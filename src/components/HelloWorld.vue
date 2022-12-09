<template>
  <v-layout class="h-100">
    <v-navigation-drawer v-model="drawer" :rail="rail" permanent @click="rail = false">
      <v-list-item prepend-avatar="/src/assets/logo.svg" title="Timendix Admin" nav>
        <template v-slot:append>
          <v-btn variant="text" @click.stop="rail = !rail">
            <arrow-bar-left-icon />
          </v-btn>
        </template>
      </v-list-item>

      <v-divider></v-divider>

      <v-list density="compact" nav>

        <v-list-item prepend-icon="mdi-monitor-dashboard" title="Dashboard" value="dashboard"></v-list-item>
        <v-list-item prepend-icon="mdi-human-male-board" title="Teachers" value="teachers"></v-list-item>
        <v-list-item prepend-icon="mdi-book-account" title="Classes" value="classes"></v-list-item>
        <v-list-item prepend-icon="mdi-calendar-text" title="Logs" value="logs"></v-list-item>
        <v-list-item prepend-icon="mdi-cog" title="Settings" value="settings"></v-list-item>
      </v-list>

      <template v-slot:append>
        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-logout" title="Logout" value="logout"></v-list-item>
        </v-list>
      </template>


    </v-navigation-drawer>
  </v-layout>
</template>


<script>
import { ArrowBarLeftIcon, LogoutIcon } from "vue-tabler-icons";

export default {
  components: { ArrowBarLeftIcon, LogoutIcon },
  data() {
    return {
      drawer: true,
      items: [
        { title: 'Home', icon: 'mdi-home-city' },
        { title: 'My Account', icon: 'mdi-account' },
        { title: 'Users', icon: 'mdi-account-group-outline' },
      ],
      rail: true,
    }
  },
}
</script>