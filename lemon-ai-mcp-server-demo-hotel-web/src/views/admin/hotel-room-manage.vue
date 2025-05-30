<template>
  <div class="hotel-list">
    <a-page-header title="酒店房间列表" style="border-bottom: 1px solid rgb(235, 237, 240)">
      <template #extra>
        <div class="select-wrapper">
          <span class="select-label">选择酒店：</span>
          <a-select
              v-model:value="selectedHotelId"
              style="width: 200px"
              placeholder="请选择酒店"
              @change="handleHotelChange"
          >
            <a-select-option v-for="hotel in hotelList" :key="hotel.id" :value="hotel.id">
              {{ hotel.name }}
            </a-select-option>
          </a-select>
          <a-button type="primary" @click="showCreateModal">创建房间</a-button>
        </div>
      </template>
    </a-page-header>
    <a-table :columns="columns" :data-source="data" :pagination="{ pageSize: 20 }">
      <template #action="{ record }">
        <a-space>
          <a-button size="small" @click="handleEdit(record)">编辑</a-button>
          <a-popconfirm
            title="确定要删除这个房间吗？"
            ok-text="确定"
            cancel-text="取消"
            @confirm="handleDelete(record)"
          >
            <a-button size="small" danger>删除</a-button>
          </a-popconfirm>
        </a-space>
      </template>
    </a-table>

    <!-- 创建房间对话框 -->
    <a-modal
        v-model:visible="createModalVisible"
        :title="isEditMode ? '编辑房间' : '创建房间'"
        @ok="handleCreateRoom"
        :confirmLoading="createLoading"
    >
      <a-form :model="createForm" layout="vertical">
        <a-form-item label="房间编号" required>
          <a-input v-model:value="createForm.no" placeholder="请输入房间编号"/>
        </a-form-item>
        <a-form-item label="所属酒店" required>
          <a-select
              v-model:value="createForm.hotelId"
              placeholder="请选择酒店"
              :options="hotelList.map(hotel => ({ label: hotel.name, value: hotel.id }))"
          />
        </a-form-item>
        <a-form-item label="房型" required>
          <a-select
              v-model:value="createForm.hotelRoomTypeId"
              placeholder="请选择房型"
              :options="roomTypeList.map(type => ({ label: type.name, value: type.id }))"
          />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import {onMounted, ref, h} from 'vue'
import HotelRoomDto from '@/model/hotel-room-dto'
import HotelDto from '@/model/hotel-dto'
import HotelRoomTypeDto from '@/model/hotel-room-type-dto'
import HotelService from '@/service/hotel-service'
import {message} from 'ant-design-vue'

const columns = [
  {
    title: '房间编号',
    dataIndex: 'no',
    key: 'no'
  },
  {
    title: '所属酒店',
    dataIndex: 'hotelId',
    key: 'hotelId',
    customRender: ({ text }: { text: string }) => {
      const hotel = hotelList.value.find(h => h.id === text)
      return hotel ? hotel.name : '-'
    }
  },
  {
    title: '房型',
    dataIndex: 'hotelRoomTypeId',
    key: 'hotelRoomTypeId',
    customRender: ({ text }: { text: string }) => {
      const roomType = roomTypeList.value.find(t => t.id === text)
      return roomType ? roomType.name : '-'
    }
  },
  {
    title: '操作',
    key: 'action',
    width: 200,
    slots: { customRender: 'action' }
  }
]

const data = ref<HotelRoomDto[]>([])
const hotelList = ref<HotelDto[]>([])
const roomTypeList = ref<HotelRoomTypeDto[]>([])
const selectedHotelId = ref<string>('')

// 创建房间相关
const createModalVisible = ref(false)
const createLoading = ref(false)
const createForm = ref<HotelRoomDto>(new HotelRoomDto())
const isEditMode = ref(false)

onMounted(() => {
  refreshHotelList()
  refreshRoomTypeList()
})

function refreshHotelList() {
  HotelService.listAllHotel()
      .then((result: HotelDto[]) => {
        hotelList.value = result
        if (result.length > 0) {
          selectedHotelId.value = result[0].id
          refreshRoomList(result[0].id)
        }
      })
      .catch(e => {
        message.error('加载酒店列表失败')
      })
}

function refreshRoomTypeList() {
  HotelService.listAllHotelRoomType()
      .then((result: HotelRoomTypeDto[]) => {
        roomTypeList.value = result
      })
      .catch(e => {
        message.error('加载房型列表失败')
      })
}

function refreshRoomList(hotelId: string) {
  const hide = message.loading('加载中..', 0)
  HotelService.listAllHotelRoom(hotelId)
      .then((result: HotelRoomDto[]) => {
        data.value = result
      })
      .catch(e => {
        message.error('加载失败')
      })
      .finally(() => {
        hide()
      })
}

function handleHotelChange(value: string) {
  if (value) {
    refreshRoomList(value)
  }
}

function handleEdit(record: HotelRoomDto) {
  isEditMode.value = true
  createForm.value = { ...record }
  createModalVisible.value = true
}

function handleDelete(record: HotelRoomDto) {
  const hide = message.loading('删除中..', 0)
  HotelService.deleteHotelRoom(record.id)
    .then(() => {
      message.success('删除成功')
      refreshRoomList(selectedHotelId.value)
    })
    .catch((e: Error) => {
      message.error('删除失败：' + e.message)
    })
    .finally(() => {
      hide()
    })
}

function showCreateModal() {
  isEditMode.value = false
  createForm.value = new HotelRoomDto()
  createForm.value.hotelId = selectedHotelId.value
  if (roomTypeList.value.length > 0) {
    createForm.value.hotelRoomTypeId = roomTypeList.value[0].id
  }
  createModalVisible.value = true
}

function handleCreateRoom() {
  createForm.value.hotelId = selectedHotelId.value
  if (!createForm.value.no) {
    message.error('请输入房间编号')
    return
  }
  if (!createForm.value.hotelId) {
    message.error('请选择所属酒店')
    return
  }
  if (!createForm.value.hotelRoomTypeId) {
    message.error('请选择房型')
    return
  }

  createLoading.value = true
  HotelService.saveHotelRoom(createForm.value)
      .then(() => {
        message.success(isEditMode.value ? '保存成功' : '创建成功')
        createModalVisible.value = false
        refreshRoomList(createForm.value.hotelId)
      })
      .catch((e: Error) => {
        message.error((isEditMode.value ? '保存' : '创建') + '失败：' + e.message)
      })
      .finally(() => {
        createLoading.value = false
      })
}
</script>

<style scoped lang="scss">
.hotel-list {
  overflow: scroll;
  height: 100%;
}

.select-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;

  .select-label {
    font-size: 14px;
    color: rgba(0, 0, 0, 0.85);
  }
}
</style>