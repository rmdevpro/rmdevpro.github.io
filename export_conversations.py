#!/usr/bin/env python3
"""
Export conversations from Dewey to Jekyll markdown files.

This script connects to Dewey (via MCP relay), queries conversations,
and exports them as markdown files in the _conversations/ directory
for the Jekyll static site.
"""

import json
import re
from datetime import datetime
from pathlib import Path
import subprocess


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def get_conversations(limit=100, offset=0):
    """Query Dewey for conversations via Claude Code MCP."""
    # This would normally use the MCP relay, but for now we'll
    # demonstrate with the structure
    print(f"Fetching conversations (limit={limit}, offset={offset})...")

    # Example: You would call this via subprocess to Claude Code MCP
    # For now, returning placeholder structure
    return {
        "conversations": [],
        "total": 0
    }


def get_conversation_messages(conversation_id):
    """Get all messages for a conversation."""
    print(f"Fetching messages for conversation {conversation_id}...")

    # Example: You would call this via subprocess to Claude Code MCP
    # For now, returning placeholder structure
    return {
        "messages": []
    }


def format_message(message):
    """Format a single message for markdown output."""
    role = message.get('role', 'unknown')
    content = message.get('content', '')
    timestamp = message.get('created_at', '')

    # Clean up role display
    role_display = {
        'user': 'User',
        'assistant': 'Assistant',
        'system': 'System'
    }.get(role.lower(), role.title())

    # Format timestamp if available
    time_str = ''
    if timestamp:
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            time_str = f" ({dt.strftime('%H:%M:%S')})"
        except:
            pass

    return f"### {role_display}{time_str}\n\n{content}\n"


def create_conversation_markdown(conversation, messages):
    """Create a markdown file for a conversation."""
    conv_id = conversation['id']
    created_at = conversation.get('created_at', '')
    metadata = json.loads(conversation.get('metadata', '{}'))
    message_count = conversation.get('message_count', len(messages))

    # Parse date
    try:
        dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        date_str = dt.strftime('%Y-%m-%d')
        date_display = dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d')
        date_display = 'Unknown'

    # Generate title from first user message or use ID
    title = f"Conversation {conv_id[:8]}"
    if messages:
        first_user_msg = next((m for m in messages if m.get('role') == 'user'), None)
        if first_user_msg:
            content = first_user_msg.get('content', '')
            # Use first line or first 100 chars as title
            title_text = content.split('\n')[0][:100].strip()
            if title_text:
                title = title_text

    # Generate filename
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"

    # Extract workflow, tags, participants from metadata
    workflow = metadata.get('workflow', metadata.get('source', 'development'))
    tags = metadata.get('tags', [])
    participants = metadata.get('participants', ['Claude'])

    # Auto-detect participants from messages if not in metadata
    if not participants or participants == ['Claude']:
        roles = set()
        for msg in messages[:10]:  # Check first 10 messages
            role = msg.get('role', '')
            if role in ['user', 'assistant']:
                roles.add(role)
        if 'assistant' in roles:
            participants = ['Claude', 'User']

    # Generate summary from first few messages
    summary = ""
    if messages and len(messages) > 1:
        first_msgs = [m.get('content', '')[:200] for m in messages[:2]]
        summary = ' '.join(first_msgs)[:200] + '...'

    # Build frontmatter
    frontmatter = f"""---
layout: conversation
title: "{title}"
date: {date_display}
workflow: {workflow}
participants: {json.dumps(participants)}
tags: {json.dumps(tags if tags else ['development'])}
message_count: {message_count}
conversation_id: {conv_id}
summary: >
  {summary}
---

"""

    # Build message content
    message_content = "\n".join(format_message(msg) for msg in messages)

    # Combine
    full_content = frontmatter + message_content

    return filename, full_content


def export_conversations(limit=None, batch_size=50):
    """Export all conversations from Dewey to markdown files."""
    output_dir = Path('_conversations')
    output_dir.mkdir(exist_ok=True)

    print(f"Exporting conversations to {output_dir}/")

    offset = 0
    total_exported = 0

    while True:
        # Get batch of conversations
        result = get_conversations(limit=batch_size, offset=offset)
        conversations = result.get('conversations', [])
        total = result.get('total', 0)

        if not conversations:
            break

        print(f"\nProcessing batch {offset}-{offset + len(conversations)} of {total}...")

        for conv in conversations:
            try:
                conv_id = conv['id']

                # Get messages
                msg_result = get_conversation_messages(conv_id)
                messages = msg_result.get('messages', [])

                # Create markdown
                filename, content = create_conversation_markdown(conv, messages)

                # Write file
                filepath = output_dir / filename
                filepath.write_text(content, encoding='utf-8')

                print(f"  ✓ {filename} ({len(messages)} messages)")
                total_exported += 1

            except Exception as e:
                print(f"  ✗ Error exporting {conv.get('id', 'unknown')}: {e}")

        offset += len(conversations)

        # Stop if we've hit the limit
        if limit and total_exported >= limit:
            break

        # Stop if we've processed all conversations
        if offset >= total:
            break

    print(f"\n✓ Exported {total_exported} conversations to {output_dir}/")
    return total_exported


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Export Dewey conversations to Jekyll markdown')
    parser.add_argument('--limit', type=int, help='Limit number of conversations to export')
    parser.add_argument('--batch-size', type=int, default=50, help='Batch size for fetching')

    args = parser.parse_args()

    # NOTE: This is a template script. To actually use it, you need to:
    # 1. Implement MCP relay communication in get_conversations() and get_conversation_messages()
    # 2. Or, extract conversation data from Dewey directly via PostgreSQL

    print("WARNING: This is a template export script.")
    print("You need to implement the actual Dewey MCP connection.")
    print("\nTo export conversations, you have two options:")
    print("1. Implement MCP relay calls in this script")
    print("2. Query PostgreSQL directly (requires credentials)")

    # Uncomment when ready:
    # export_conversations(limit=args.limit, batch_size=args.batch_size)


if __name__ == '__main__':
    main()
