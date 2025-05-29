<template>
  <div class="hotel-list">
    <a-page-header title="酒店门店管理" style="border-bottom: 1px solid rgb(235, 237, 240)">
      <template #extra>
      </template>
    </a-page-header>
    <a-table :columns="columns" :data-source="data" :pagination="{ pageSize: 20 }">
    </a-table>
  </div>
</template>

<script setup lang="ts">
import {onMounted, ref} from 'vue'
import {message} from 'ant-design-vue'
import DateUtils from '@/utils/date-utils.ts'
import HotelService from '@/service/hotel-service.ts'
import type HotelDto from '@/model/hotel-dto.ts'

const dateUtils = DateUtils
const columns = [
  {
    title: '酒店名称',
    dataIndex: 'name',
    key: 'name'
  },
  {
    title: '酒店地址',
    dataIndex: 'address',
    key: 'address'
  },
  {
    title: '酒店介绍',
    dataIndex: 'description',
    key: 'description'
  }
]

const data = ref<HotelDto[]>([])

onMounted(() => {
  refreshUserList()
})

function refreshUserList() {
  const hide = message.loading('加载中..', 0)
  HotelService.listAllHotel()
      .then((result: HotelDto[]) => {
        data.value = result
        console.log('数据是', data.value)
      })
      .catch(e => {
        message.error('加载失败')
      })
      .finally(() => {
        hide()
      })
}
</script>

<style scoped lang="scss">
.user-list {
  overflow: scroll;
  height: 100%;
}
</style>