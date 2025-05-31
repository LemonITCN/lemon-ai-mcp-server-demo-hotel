<template>
  <div class="chat-page">
    <div class="chat-container">
      <div class="chat-header">
        <div class="ai-avatar">AI</div>
        <div class="header-text">
          <h2>AI 助手</h2>
          <p>在线咨询</p>
        </div>
      </div>

      <div class="chat-messages" ref="messagesContainer" @wheel.passive="handleWheel">
        <div v-for="(message, index) in messages"
             :key="index"
             :class="['message', message.type]">
          <div v-if="message.type === 'user'" class="avatar">
            <img :src="userAvatar" alt="用户头像" class="user-avatar"/>
          </div>
          <div :class="['message-content', message.type]">
            <div v-if="message.type === 'user'" class="message-text">{{ message.content }}</div>
            <div v-else class="markdown-content" v-html="renderMarkdown(message.content)"></div>
          </div>
        </div>
      </div>

      <div class="chat-input">
        <textarea
            v-model="inputMessage"
            @keydown.enter.prevent="sendMessage"
            placeholder="输入消息..."
            :disabled="isLoading"
        ></textarea>
        <button
            @click="sendMessage"
            :disabled="isLoading || !inputMessage.trim()"
            class="send-button"
        >
          <span v-if="!isLoading">发送</span>
          <span v-else class="loading">发送中...</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {nextTick, onMounted, ref} from 'vue'
import MarkdownIt from 'markdown-it'
import userAvatar from '@/assets/user-avatar.svg'
import {fetchEventSource} from '@microsoft/fetch-event-source'
import {HttpUtils} from '@/utils/http-utils.ts'

const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
})

const renderMarkdown = (content: string) => {
  return md.render(content)
}

interface Message {
  type: 'user' | 'ai'
  content: string
}

const messages = ref<Message[]>([])
const inputMessage = ref('')
const isLoading = ref(false)
const messagesContainer = ref<HTMLElement | null>(null)
// 会话id
const conversationId = ref('')

const scrollToBottom = async () => {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const formatTime = () => {
  const now = new Date()
  return now.toLocaleTimeString('zh-CN', {hour: '2-digit', minute: '2-digit'})
}

const sendMessage = async () => {
  if (!inputMessage.value.trim() || isLoading.value) return

  const userMessage: Message = {
    type: 'user',
    content: inputMessage.value,
    time: ''
  }

  messages.value.push(userMessage)
  await scrollToBottom()

  // 模拟AI响应
  isLoading.value = true
  const controller = new AbortController()
  fetchEventSource(HttpUtils.getBaeUrl() + '/ai-chat/send-message', {
    signal: controller.signal,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      message: inputMessage.value,
      conversationId: conversationId.value
    }),
    onmessage(message) {
      const messageData = JSON.parse(message.data)
      console.log('接收到消息', messageData)
      conversationId.value = messageData.conversation_id
      if (messageData.type === 'message') {
        const aiMessage: Message = {
          type: 'ai',
          content: messageData.content
        }
        messages.value.push(aiMessage)
        isLoading.value = false
        scrollToBottom()
      }
    },
    onerror(err) {
      console.error('连接出错', err)
      controller.abort()
    }
  })
  inputMessage.value = ''
}

const handleWheel = (e: WheelEvent) => {
  const container = messagesContainer.value
  if (!container) return

  const {scrollTop, scrollHeight, clientHeight} = container

  // 如果已经滚动到底部，且继续向下滚动，则阻止默认行为
  if (scrollTop + clientHeight >= scrollHeight && e.deltaY > 0) {
    e.preventDefault()
  }

  // 如果已经滚动到顶部，且继续向上滚动，则阻止默认行为
  if (scrollTop <= 0 && e.deltaY < 0) {
    e.preventDefault()
  }
}

onMounted(() => {
  // 添加欢迎消息
  messages.value.push({
    type: 'ai',
    content: `### 你好呀，欢迎咨询VT酒店

请问您想住什么房间？`
  })
})
</script>

<style lang="scss" scoped>
@use "sass:color";

// 变量定义
$primary-color: #007AFF;
$primary-hover: #0056b3;
$background-color: #f5f5f5;
$white: #ffffff;
$border-color: #eee;
$text-color: #333;
$text-light: #999;
$gray: #666;
$shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.1);
$shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);

.chat-page {
  height: 100%;
  background-color: $background-color;
  overflow: hidden;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: $background-color;
  border-radius: 12px;
  overflow: hidden;
  position: relative;

  .chat-header {
    padding: 0.75rem 1rem;
    background-color: $primary-color;
    color: $white;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    border-bottom: 1px solid rgba($white, 0.1);
    flex-shrink: 0;

    .ai-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background-color: $white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      color: $primary-color;
      font-size: 0.8rem;
    }

    .header-text {
      flex: 1;

      h2 {
        margin: 0;
        font-size: 0.9rem;
      }

      p {
        margin: 0;
        font-size: 0.75rem;
        opacity: 0.8;
      }
    }
  }

  .chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    overscroll-behavior: contain;
    -webkit-overflow-scrolling: touch;

    &::-webkit-scrollbar {
      width: 4px;
    }

    &::-webkit-scrollbar-track {
      background: transparent;
    }

    &::-webkit-scrollbar-thumb {
      background: rgba($text-color, 0.2);
      border-radius: 2px;
    }

    .message {
      display: flex;
      gap: 0.5rem;
      max-width: 85%;

      &.user {
        align-self: flex-end;
        flex-direction: row-reverse;

        .message-content {
          background-color: $primary-color;
          color: $white;
          border-radius: 12px 2px 12px 12px;
        }
      }

      &.ai {
        align-self: flex-start;
        margin-left: 8px;

        .message-content {
          background-color: #ffffff;
          color: $text-color;
          border-radius: 8px;
          box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
          padding: 0.8rem 1rem;
        }
      }

      .avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
        font-size: 0.8rem;
        overflow: hidden;

        .user-avatar {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }
      }

      .message-content {
        padding: 0.6rem 0.8rem;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);

        .message-text {
          font-size: 0.9rem;
          line-height: 1.4;
        }

        .markdown-content {
          font-size: 0.9rem;
          line-height: 1.6;

          :deep(h1) {
            font-size: 1.5rem;
            margin: 0 0 1rem 0;
            color: $text-color;
          }

          :deep(h2) {
            font-size: 1.2rem;
            margin: 1rem 0 0.8rem 0;
            color: $text-color;
          }

          :deep(p) {
            margin: 0 0 0.8rem 0;
            color: $text-color;
          }

          :deep(pre) {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 6px;
            overflow-x: auto;
            margin: 0.8rem 0;
            border: 1px solid #e9ecef;
          }

          :deep(code) {
            background-color: #f8f9fa;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: monospace;
            border: 1px solid #e9ecef;
          }

          :deep(ul), :deep(ol) {
            margin: 0.8rem 0;
            padding-left: 1.5rem;
            color: $text-color;
          }

          :deep(blockquote) {
            border-left: 4px solid #e9ecef;
            margin: 0.8rem 0;
            padding: 0.5rem 0 0.5rem 1rem;
            color: $gray;
            background-color: #f8f9fa;
            border-radius: 0 4px 4px 0;
          }

          :deep(table) {
            border-collapse: collapse;
            width: 100%;
            margin: 0.8rem 0;

            th, td {
              border: 1px solid #e9ecef;
              padding: 0.5rem;
              text-align: left;
            }

            th {
              background-color: #f8f9fa;
            }
          }
        }
      }
    }
  }

  .chat-input {
    padding: 0.75rem;
    background-color: $white;
    border-top: 1px solid rgba($text-color, 0.1);
    display: flex;
    gap: 0.5rem;
    flex-shrink: 0;

    textarea {
      flex: 1;
      padding: 0.6rem 0.8rem;
      border: 1px solid rgba($text-color, 0.2);
      border-radius: 8px;
      resize: none;
      font-family: inherit;
      font-size: 0.9rem;
      line-height: 1.4;
      max-height: 100px;
      min-height: 36px;
      transition: border-color 0.3s;

      &:focus {
        outline: none;
        border-color: $primary-color;
      }
    }

    .send-button {
      padding: 0.6rem 1.2rem;
      background-color: $primary-color;
      color: $white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: background-color 0.3s;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;

      &:hover {
        background-color: color.adjust($primary-color, $lightness: -10%);
      }

      &:disabled {
        background-color: $gray;
        cursor: not-allowed;
      }
    }
  }
}

.loading {
  opacity: 0.7;
}
</style> 