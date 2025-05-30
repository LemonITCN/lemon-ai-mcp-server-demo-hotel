<template>
  <RouterView class="root-router-view"/>
</template>

<script setup lang="ts">
import {RouterView, useRouter, useRoute} from 'vue-router'
import {onMounted, ref} from 'vue'
import {HttpUtils} from '@/utils/http-utils.ts'

const $router = useRouter()
const $route = useRoute()

const ready = ref(false)

onMounted(() => {
  // 如果是chat路径，直接返回，不进行token验证
  console.log(JSON.stringify($route))
  // if ($route.path === '/chat' || $route.path === '/client-home') {
  //   ready.value = true
  //   return
  // }

  if (localStorage.getItem('token')) {
    HttpUtils.addDefaultHeader('LEMON-USER-TOKEN', localStorage.getItem('token')!)
  } else {
    // $router.replace('/login')
  }
  ready.value = true
})
</script>

<style scoped lang="scss">
.root-router-view {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: #ffffff;
  color: #333333;
}
</style>
