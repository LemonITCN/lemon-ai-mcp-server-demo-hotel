<template>
  <div class="view-login">
    <div class="login-form">
      <div class="login-form-title">
        酒店管理后台
      </div>
      <div class="field-item">
        <div class="field-title">账号</div>
        <a-input type="text" v-model:value="phone" class="field-input"/>
      </div>
      <div class="field-item">
        <div class="field-title">密码</div>
        <a-input type="password" v-model:value="password" class="field-input"/>
      </div>
      <view class="action-line">
        <a-button type="primary" class="login-button" @click="login"
                  :disabled="phone.length < 10 || password.length < 4">登录
        </a-button>
      </view>
    </div>
  </div>
</template>

<script setup lang="ts">
import CryptoJS from 'crypto-js'
import {ref} from 'vue'
import UserService from '@/service/user-service.ts'
import {HttpUtils} from '@/utils/http-utils.ts'
import {message} from 'ant-design-vue'
import {useRouter} from 'vue-router'

// 登录手机号码
const phone = ref('')
// 登录密码
const password = ref('')

const $router = useRouter()

function encryptPassword(password: string): string {
  return CryptoJS.SHA256(password).toString(CryptoJS.enc.Hex)
}

function login() {
  const passwordSecret = encryptPassword(password.value)
  UserService.login(phone.value, passwordSecret)
      .then((res) => {
        console.log('add token', res.token)
        HttpUtils.addDefaultHeader('LEMON-USER-TOKEN', res.token)
        localStorage.setItem('token', res.token)
        $router.replace({
          path: '/'
        })
      })
      .catch((err) => {
        message.error('登录失败' + err.message)
      })
}
</script>

<style lang="scss" scoped>
.view-login {
  .background-img {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
  }

  .login-form {
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(10px);
    position: absolute;
    width: 400px;
    height: 400px;
    left: calc(50% - 200px);
    top: calc(50% - 200px);
    padding: 20px 40px;
    border: 1px solid #dddddd;

    .login-form-title {
      margin: 30px 0 40px 0;
      text-align: center;
      font-size: 18px;
      font-weight: bold;
    }

    .field-item {
      margin-bottom: 10px;

      .field-title {
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 10px;
      }

      .field-input {
        background: rgba(255, 255, 255, 0.5);
      }
    }

    .action-line {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      margin-top: 50px;

      .login-button {
        width: 80%;
        height: 40px;
      }
    }
  }
}
</style>
