<template>
  <div class="home-page">
    <!-- 顶部导航 -->
    <header class="header">
      <div class="header-content">
        <div class="logo">VT ホテル</div>
        <nav class="nav">
          <a href="#home" class="active">ホーム</a>
          <a href="#rooms">客室</a>
          <a href="#dining">レストラン</a>
          <a href="#facilities">施設</a>
          <a href="#about">ホテルについて</a>
          <a @click="handleAdminClick" class="admin-link">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 1L3 5V11C3 16.55 6.84 21.74 12 23C17.16 21.74 21 16.55 21 11V5L12 1ZM12 11.99H19C18.47 16.11 15.72 19.78 12 20.93V12H5V6.3L12 3.19V11.99Z" fill="currentColor"/>
            </svg>
            管理画面
          </a>
        </nav>
      </div>
    </header>

    <!-- 主视觉区域 -->
    <section class="hero">
      <div class="hero-content">
        <h1>VT ホテルへようこそ</h1>
        <p>贅沢と快適さの完璧な調和を体験</p>
        <button class="cta-button">予約する</button>
      </div>
    </section>

    <!-- 特色服务 -->
    <section class="features">
      <div class="feature-card">
        <i class="icon-bed"></i>
        <h3>ラグジュアリールーム</h3>
        <p>最高の快適さを提供する、こだわりの客室</p>
      </div>
      <div class="feature-card">
        <i class="icon-dining"></i>
        <h3>美食体験</h3>
        <p>ミシュラン星付きシェフによる特別な料理体験</p>
      </div>
      <div class="feature-card">
        <i class="icon-spa"></i>
        <h3>スパ</h3>
        <p>専門セラピストによる心身を癒すスパサービス</p>
      </div>
    </section>

    <!-- 房间展示 -->
    <section class="rooms" id="rooms">
      <h2>おすすめ客室</h2>
      <div class="room-grid">
        <div class="room-card">
          <img src="https://picsum.photos/400/300" alt="デラックスツインルーム">
          <div class="room-info">
            <h3>デラックスツインルーム</h3>
            <p>45㎡ | ツインベッド | シティビュー</p>
            <div class="room-price">¥8,880/泊</div>
          </div>
        </div>
        <div class="room-card">
          <img src="https://picsum.photos/400/301" alt="エグゼクティブルーム">
          <div class="room-info">
            <h3>エグゼクティブルーム</h3>
            <p>65㎡ | キングベッド | オーシャンビュー</p>
            <div class="room-price">¥12,880/泊</div>
          </div>
        </div>
        <div class="room-card">
          <img src="https://picsum.photos/400/302" alt="プレジデンシャルスイート">
          <div class="room-info">
            <h3>プレジデンシャルスイート</h3>
            <p>120㎡ | キングベッド | パノラマビュー</p>
            <div class="room-price">¥28,880/泊</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 悬浮聊天按钮 -->
    <div class="chat-float">
      <a-popover
        placement="leftBottom"
        trigger="click"
        :overlayClassName="'chat-popover'"
        :overlayStyle="{ width: '400px', height: '600px' }"
        :getPopupContainer="(triggerNode) => triggerNode.parentNode"
      >
        <template #content>
          <chat-view />
        </template>
        <div class="chat-button">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 2H4C2.9 2 2 2.9 2 4V22L6 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2ZM20 16H5.2L4 17.2V4H20V16Z" fill="currentColor"/>
            <path d="M7 9H17V11H7V9ZM7 12H14V14H7V12Z" fill="currentColor"/>
          </svg>
        </div>
      </a-popover>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Popover } from 'ant-design-vue'
import ChatView from './chat-view.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const handleAdminClick = () => {
  const token = localStorage.getItem('token')
  HttpUtils.addDefaultHeader('LEMON-USER-TOKEN', token)
  if (token) {
    router.push('/admin/hotel')
  } else {
    router.push('/login')
  }
}
</script>

<style lang="scss" scoped>
@use "sass:color";

// 变量定义
$primary-color: #1a1a1a;
$secondary-color: #d4af37;
$text-color: #333;
$white: #ffffff;
$gray-light: #f5f5f5;
$gray: #666;

.home-page {
  min-height: 100vh;
}

.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: rgba($white, 0.95);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 100;

  .header-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: $primary-color;
  }

  .nav {
    display: flex;
    gap: 2rem;
    align-items: center;

    a {
      color: $text-color;
      text-decoration: none;
      font-weight: 500;
      transition: color 0.3s;
      display: flex;
      align-items: center;
      gap: 0.5rem;

      &:hover, &.active {
        color: $secondary-color;
      }

      &.admin-link {
        background: linear-gradient(135deg, $secondary-color, color.adjust($secondary-color, $lightness: -15%));
        color: $white;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-size: 0.9rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;

        svg {
          width: 16px;
          height: 16px;
        }

        &:hover {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
          color: $white;
        }

        &:active {
          transform: translateY(0);
        }
      }
    }
  }
}

.hero {
  height: 100vh;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
              url('https://picsum.photos/1920/1080') center/cover;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: $white;

  .hero-content {
    h1 {
      font-size: 3.5rem;
      margin-bottom: 1rem;
    }

    p {
      font-size: 1.5rem;
      margin-bottom: 2rem;
    }
  }

  .cta-button {
    padding: 1rem 2rem;
    font-size: 1.2rem;
    background-color: $secondary-color;
    color: $white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;

    &:hover {
      background-color: color.adjust($secondary-color, $lightness: -10%);
    }
  }
}

.features {
  padding: 4rem 2rem;
  background-color: $gray-light;
  display: flex;
  justify-content: center;
  gap: 2rem;

  .feature-card {
    flex: 1;
    max-width: 300px;
    padding: 2rem;
    background-color: $white;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

    i {
      font-size: 2.5rem;
      color: $secondary-color;
      margin-bottom: 1rem;
    }

    h3 {
      margin-bottom: 1rem;
      color: $text-color;
    }

    p {
      color: $gray;
    }
  }
}

.rooms {
  padding: 4rem 2rem;
  max-width: 1200px;
  margin: 0 auto;

  h2 {
    text-align: center;
    margin-bottom: 2rem;
    font-size: 2rem;
    color: $text-color;
  }

  .room-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  .room-card {
    background-color: $white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;

    &:hover {
      transform: translateY(-5px);
    }

    img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .room-info {
      padding: 1.5rem;

      h3 {
        margin-bottom: 0.5rem;
        color: $text-color;
      }

      p {
        color: $gray;
        margin-bottom: 1rem;
      }

      .room-price {
        font-size: 1.2rem;
        color: $secondary-color;
        font-weight: bold;
      }
    }
  }
}

.chat-float {
  position: fixed;
  left: 30px;
  bottom: 30px;
  z-index: 1000;

  .chat-button {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, $secondary-color, color.adjust($secondary-color, $lightness: -15%));
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;

    svg {
      width: 28px;
      height: 28px;
      color: $white;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
    }

    &:hover {
      transform: scale(1.1);
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);

      svg {
        transform: scale(1.1);
      }
    }

    &:active {
      transform: scale(0.95);
    }
  }
}

:deep(.chat-popover) {
  position: fixed !important;
  left: 100px !important;
  bottom: 30px !important;
  top: auto !important;
  right: auto !important;
  transform: none !important;

  .ant-popover-inner {
    padding: 0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
    height: 600px;
  }
  
  .ant-popover-inner-content {
    padding: 0;
    height: 100%;
  }

  .ant-popover-arrow {
    display: none;
  }
}
</style> 