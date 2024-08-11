import Vue from "vue";
import VueRouter from "vue-router";
import GamesLibrary from "../components/GamesLibrary.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/games",
    name: "Games Library",
    component: GamesLibrary,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
