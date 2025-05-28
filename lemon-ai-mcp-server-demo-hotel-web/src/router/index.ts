import {createRouter, createWebHashHistory} from 'vue-router'
import Login from '../views/login.vue'
import Main from '@/views/main.vue'
import HotelManage from '@/views/hotel-manage.vue'
import HotelRoomTypeManage from '@/views/hotel-room-type-manage.vue'
import HotelRoomManage from '@/views/hotel-room-manage.vue'
import OrderManage from '@/views/order-manage.vue'

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            component: Login
        },
        {
            path: '/',
            component: Main,
            children: [
                {
                    path: 'hotel',
                    component: HotelManage
                },
                {
                    path: 'hotel-room-type',
                    component: HotelRoomTypeManage
                },
                {
                    path: 'hotel-room',
                    component: HotelRoomManage
                },
                {
                    path: 'order',
                    component: OrderManage
                }
            ]
        }
    ]
})

export default router
