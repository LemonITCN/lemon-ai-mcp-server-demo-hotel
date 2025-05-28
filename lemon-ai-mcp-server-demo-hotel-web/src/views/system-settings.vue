<template>
  <div class="system-settings">
    <a-page-header title="系统设置" style="border-bottom: 1px solid rgb(235, 237, 240)">
      <template #extra>
      </template>
    </a-page-header>
    <a-table :columns="columns" :data-source="systemSettings" :pagination="{ pageSize: 20 }">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'actions'">
          <a-button size="small" :icon="h(EditOutlined)" @click="edit(record)">设置</a-button>
        </template>
      </template>
    </a-table>
    <a-modal v-model:open="editDialogShowState" title="设置" @ok="submit">
      <div class="form-content">
        <div class="form-item">
          <div class="title">设置项名称</div>
          <a-input :value="editingSystemSetting!.name" disabled class="field"/>
        </div>
        <div class="form-item">
          <div class="title">设置项值</div>
          <a-input v-model:value="editingSystemSetting!.value" class="field"/>
        </div>
      </div>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import type SystemSettingsDto from '@/model/system-settings-dto.ts'
import {h, onMounted, ref} from 'vue'
import SystemSettingsService from '@/service/system-settings-service.ts'
import {EditOutlined} from '@ant-design/icons-vue'
import {message} from 'ant-design-vue'

const systemSettings = ref<SystemSettingsDto[]>([])
// 列
const columns = [
  {
    title: '设置项目',
    dataIndex: 'name',
    key: 'name'
  },
  {
    title: '设置项值',
    dataIndex: 'value',
    key: 'value'
  },
  {
    title: '操作',
    dataIndex: 'actions',
    key: 'actions'
  }
]
// 编辑对话框状态
const editDialogShowState = ref(false)
// 编辑中的设置项
const editingSystemSetting = ref<SystemSettingsDto | null>(null)

onMounted(() => {
  refreshSettings()
})

function refreshSettings() {
  SystemSettingsService.listAllSettings()
      .then((res) => {
        systemSettings.value = res
      })
}

function edit(record: SystemSettingsDto) {
  editingSystemSetting.value = JSON.parse(JSON.stringify(record))
  editDialogShowState.value = true
}

function submit() {
  const hide = message.loading('正在保存设置项...', 0)
  SystemSettingsService.update(editingSystemSetting.value!)
      .then(() => {
        refreshSettings()
        editDialogShowState.value = false
        message.success('设置项保存成功')
      })
      .catch((e) => {
        message.error('设置项保存失败')
      })
      .finally(() => {
        hide()
      })
}
</script>

<style scoped lang="scss">
.form-content {
  padding: 10px 0;

  .form-item {
    margin-bottom: 10px;

    .title {
      margin-bottom: 4px;
    }

    .field {

    }
  }
}

</style>