<template>
  <div class="view-main">
    <div class="menu-area">
      <div class="user-info">
        <img src="../../assets/images/logo.png" class="logo"/>
        <div class="nickname">{{ userInfo.nickname }}</div>
        <a-popconfirm
            title="您确认要退出登录吗？"
            ok-text="退出登录" placement="right"
            cancel-text="取消"
            @confirm="logout">
          <a-button class="logout-btn">退出登录</a-button>
        </a-popconfirm>
      </div>
      <a-menu class="menu"
              v-model:selectedKeys="selectedKeys"
              style="width: 256px"
              mode="vertical"
              :items="items"
      />
    </div>
    <div class="content-area">
      <router-view class="content-router"/>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {computed, h, onMounted, ref, watch} from 'vue'
import {FileDoneOutlined, FileImageOutlined, HomeOutlined, RobotOutlined} from '@ant-design/icons-vue'
import {DataStore} from '@/stores/data-store.ts'
import {useRouter} from 'vue-router'
import {HttpUtils} from '@/utils/http-utils.ts'

const selectedKeys = ref(['hotel'])
const items = ref([
  {
    key: 'hotel-room-type',
    icon: () => h(HomeOutlined),
    label: '房型管理',
    title: 'hotel_room_type'
  },
  {
    key: 'hotel',
    icon: () => h(FileDoneOutlined),
    label: '酒店门店管理',
    title: 'hotel'
  },
  {
    key: 'hotel-room',
    icon: () => h(RobotOutlined),
    label: '房间管理',
    title: 'hotel_room'
  },
  {
    key: 'order',
    icon: () => h(FileImageOutlined),
    label: '订单管理',
    title: 'order'
  }
])

const userInfo = computed(() => DataStore().userInfo)
const $router = useRouter()

watch(selectedKeys, () => {
  if (selectedKeys.value.length > 0) {
    $router.push({path: '/admin/' + selectedKeys.value[0]})
  }
}, {immediate: true})

onMounted(() => {
})

function logout() {
  HttpUtils.removeDefaultHeader('LEMON-USER-TOKEN')
  localStorage.removeItem('token')
  $router.push({path: '/login'})
}
</script>
<style scoped lang="scss">
.view-main {
  display: flex;
  flex-direction: row;

  .menu-area {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    border-right: 1px solid #dddddd;
    width: 256px;
    min-width: 256px;
    position: relative;
    overflow: scroll;
    background: #f0f0f0;

    .user-info {
      height: 180px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 999;

      .logo {
        width: 170px;
        height: 60px;
        border-radius: 110px;
        object-fit: contain;
      }

      .nickname {
        margin-top: 18px;
      }

      .logout-btn {
        margin-top: 10px;
      }
    }

    .menu {
      flex-grow: 1;
      border: none;
      backdrop-filter: blur(10px);
      background: rgba(255, 255, 255, 0.3);
    }
  }

  .content-area {
    flex-grow: 1;
  }
}
</style>
