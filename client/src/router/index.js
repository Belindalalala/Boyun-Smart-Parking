import { createRouter, createWebHistory } from 'vue-router';
import ViewUser from "../pages/ViewUser.vue"
import AddUser from "../pages/AddUser.vue"
import UpdateUser from "../pages/UpdateUser.vue"
import Login from '../pages/Login.vue';
import View from '../pages/View.vue';
import AddCar from '../pages/AddCar.vue';
import UpdateCar from '../pages/UpdateCar.vue';
import { authState } from "../authState"; // 引入全局认证状态
import ViewRecord from '../pages/ViewRecord.vue';
import AddRecord from '../pages/AddRecord.vue';
import UpdateRecord from '../pages/UpdateRecord.vue';
import ViewCar from '../pages/ViewCar.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/user",
      name: "user",
      component: ViewUser
    },
    {
      path: "/user/add",
      name: "adduser",
      component: AddUser
    },
    {
      path: "/user/update/:id",
      name: "updateuser",
      component: UpdateUser
    },
    {
      path: "/car",
      name: "car",
      component: ViewCar
    },
    {
      path: "/car/add",
      name: "addcar",
      component: AddCar
    },
    {
      path: "/car/update/:id",
      name: "updatecar",
      component: UpdateCar
    },
    {
      path: "/record",
      name: "record",
      component: ViewRecord
    },
    {
      path: "/record/add",
      name: "addrecord",
      component: AddRecord
    },
    {
      path: "/record/update/:id",
      name: "updaterecord",
      component: UpdateRecord
    },
    {
      path: "/view",
      name: "view",
      component: View,
      meta: { requiresAuth: true }, // 需要登录访问
    },
    {
      path: "/login",
      name: "login",
      component: Login
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !authState.isAuthenticated) {
    next("/login"); // 跳转到登录页
  } else if (to.path === "/login" && authState.isAuthenticated) {
    next("/"); // 如果已登录，访问登录页时重定向到主页
  } else {
    next(); // 否则放行
  }
});


export default router;