<template>
  <div class="hotel-list">
    <a-page-header title="酒店房型列表" style="border-bottom: 1px solid rgb(235, 237, 240)">
      <template #extra>
      </template>
    </a-page-header>
    <a-table :columns="columns" :data-source="data" :pagination="{ pageSize: 20 }">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'price'">
          ¥{{ record.price }}
        </template>
      </template>
    </a-table>
  </div>
</template>

<script setup lang="ts">
import {onMounted, ref} from 'vue'
import type HotelRoomTypeDto from '@/model/hotel-room-type-dto'
import HotelService from '@/service/hotel-service'
import {message} from 'ant-design-vue'

const columns = [
  {
    title: '房型名称',
    dataIndex: 'name',
    key: 'name'
  },
  {
    title: '所属酒店',
    dataIndex: 'hotelName',
    key: 'hotelName'
  },
  {
    title: '可住人数',
    dataIndex: 'people_count',
    key: 'people_count'
  },
  {
    title: '价格',
    dataIndex: 'price',
    key: 'price'
  },
  {
    title: '房型介绍',
    dataIndex: 'description',
    key: 'description'
  }
]

const data = ref<HotelRoomTypeDto[]>([])

onMounted(() => {
  refreshRoomTypeList()
})

function refreshRoomTypeList() {
  const hide = message.loading('加载中..', 0)
  HotelService.listAllHotelRoomType()
      .then((result: HotelRoomTypeDto[]) => {
        data.value = result
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
.hotel-list {
  overflow: scroll;
  height: 100%;
}
</style>