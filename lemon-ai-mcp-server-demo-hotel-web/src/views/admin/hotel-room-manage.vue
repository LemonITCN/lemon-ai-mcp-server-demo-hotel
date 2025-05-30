<template>
  <div class="hotel-list">
    <a-page-header title="酒店房间列表" style="border-bottom: 1px solid rgb(235, 237, 240)">
      <template #extra>
      </template>
    </a-page-header>
    <a-table :columns="columns" :data-source="data" :pagination="{ pageSize: 20 }">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'avatar'">
          <img :src="record.avatarUrl" style="width: 40px;height: 40px;border-radius: 6px"/>
        </template>
        <template v-if="column.key === 'vipRechargeTime'">
          {{
            record.vipRechargeTime ? dateUtils.format(new Date(record.vipRechargeTime), 'yyyy-MM-dd hh:mm:ss') : '非会员'
          }}
        </template>
      </template>
    </a-table>
  </div>
</template>

<script setup lang="ts">
import {onMounted, ref} from 'vue'
import type UserDto from '@/model/user-dto.ts'
import UserService from '@/service/user-service.ts'
import {message} from 'ant-design-vue'
import DateUtils from '@/utils/date-utils.ts'

const dateUtils = DateUtils
const columns = [
  {
    title: '头像',
    dataIndex: 'avatar',
    key: 'avatar'
  },
  {
    title: '昵称',
    dataIndex: 'nickname',
    key: 'nickname'
  },
  {
    title: '手机号码',
    dataIndex: 'phone',
    key: 'phone'
  },
  {
    title: 'VIP充值时间',
    key: 'vipRechargeTime',
    dataIndex: 'vipRechargeTime'
  }
]

const data = ref<UserDto[]>([])

onMounted(() => {
  refreshUserList()
})

function refreshUserList() {
  const hide = message.loading('加载中..', 0)
  UserService.listAllUser()
      .then((result: UserDto[]) => {
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
.user-list {
  overflow: scroll;
  height: 100%;
}
</style>