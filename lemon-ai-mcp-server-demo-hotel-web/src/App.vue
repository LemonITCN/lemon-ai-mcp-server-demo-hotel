<template>
  <RouterView class="root-router-view"/>
</template>

<script setup lang="ts">
import {RouterView, useRouter} from 'vue-router'
import {onMounted, ref} from 'vue'
import {HttpUtils} from '@/utils/http-utils.ts'

const $router = useRouter()

const ready = ref(false)

onMounted(() => {
  if (localStorage.getItem('token')) {
    HttpUtils.addDefaultHeader('LEMON-USER-TOKEN', localStorage.getItem('token')!)
    $router.push({path: '/'})
  } else {
    $router.replace('/login')
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
