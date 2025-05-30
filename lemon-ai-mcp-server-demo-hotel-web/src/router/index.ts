import HotelManage from '@/views/admin/hotel-manage.vue'
import HotelRoomManage from '@/views/admin/hotel-room-manage.vue'
import HotelRoomTypeManage from '@/views/admin/hotel-room-type-manage.vue'
import Main from '@/views/admin/main.vue'
import OrderManage from '@/views/admin/order-manage.vue'
import ChatView from '@/views/client/chat-view.vue'
import HomeView from '@/views/client/home-view.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/admin/login.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            children: [
                {
                    path: '/home',
                    component: HomeView
                },
                {
                    path: '/login',
                    component: Login
                },
                {
                    path: '/admin',
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
                },
                {
                    path: '/chat',
                    component: ChatView
                }
            ]
        },
    ]
})

export default router
