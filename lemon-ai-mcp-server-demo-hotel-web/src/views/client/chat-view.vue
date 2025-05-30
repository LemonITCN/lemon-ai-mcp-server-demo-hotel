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
      
      <div class="chat-messages" ref="messagesContainer">
        <div v-for="(message, index) in messages" 
             :key="index" 
             :class="['message', message.type]">
          <div class="avatar">
            <span :class="message.type === 'user' ? 'user-avatar' : 'ai-avatar'">{{ message.type === 'user' ? 'U' : 'AI' }}</span>
          </div>
          <div class="message-content">
            <div class="message-text">{{ message.content }}</div>
            <div class="message-time">{{ message.time }}</div>
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
import { ref, onMounted, nextTick } from 'vue'
import userAvatar from '@/assets/user-avatar.svg'
import aiAvatar from '@/assets/ai-avatar.svg'

interface Message {
  type: 'user' | 'ai'
  content: string
  time: string
}

const messages = ref<Message[]>([])
const inputMessage = ref('')
const isLoading = ref(false)
const messagesContainer = ref<HTMLElement | null>(null)

const scrollToBottom = async () => {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const formatTime = () => {
  const now = new Date()
  return now.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
}

const sendMessage = async () => {
  if (!inputMessage.value.trim() || isLoading.value) return

  const userMessage: Message = {
    type: 'user',
    content: inputMessage.value,
    time: formatTime()
  }

  messages.value.push(userMessage)
  inputMessage.value = ''
  await scrollToBottom()

  // 模拟AI响应
  isLoading.value = true
  setTimeout(() => {
    const aiMessage: Message = {
      type: 'ai',
      content: '这是一个模拟的AI响应消息。',
      time: formatTime()
    }
    messages.value.push(aiMessage)
    isLoading.value = false
    scrollToBottom()
  }, 1000)
}

onMounted(() => {
  // 添加欢迎消息
  messages.value.push({
    type: 'ai',
    content: '你好！我是AI助手，有什么我可以帮你的吗？',
    time: formatTime()
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
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: $background-color;
  border-radius: 12px;
  overflow: hidden;

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

      &.user-message {
        align-self: flex-end;
        flex-direction: row-reverse;

        .message-content {
          background-color: $primary-color;
          color: $white;
          border-radius: 12px 2px 12px 12px;
        }
      }

      &.ai-message {
        align-self: flex-start;

        .message-content {
          background-color: $white;
          color: $text-color;
          border-radius: 2px 12px 12px 12px;
        }
      }

      .avatar {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
        font-size: 0.8rem;

        &.user-avatar {
          background-color: $primary-color;
          color: $white;
        }

        &.ai-avatar {
          background-color: $white;
          color: $primary-color;
        }
      }

      .message-content {
        padding: 0.6rem 0.8rem;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);

        .message-text {
          font-size: 0.9rem;
          line-height: 1.4;
        }

        .message-time {
          font-size: 0.7rem;
          margin-top: 0.2rem;
          opacity: 0.7;
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