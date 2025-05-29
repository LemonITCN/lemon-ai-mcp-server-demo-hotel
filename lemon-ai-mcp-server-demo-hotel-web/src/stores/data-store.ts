import {defineStore} from 'pinia'
import {ref} from 'vue'
import UserDto from '@/model/user-dto.ts'

export const DataStore = defineStore('data-store', () => {

    const userInfo = ref(new UserDto())

    function setUserInfo(user: UserDto) {
        userInfo.value = user
    }

    return {
        userInfo,
        setUserInfo
    }
})