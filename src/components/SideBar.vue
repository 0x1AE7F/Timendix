<template>
  <v-navigation-drawer elevation="1" v-model="drawer" :rail="rail" permanent @click="rail = false">
    <v-list-item prepend-avatar="/src/assets/logo.svg" title="Timendix Admin" nav>
      <template v-slot:append>
        <v-btn prepend-icon="mdi-arrow-expand-left" variant="text" @click.stop="rail = !rail" />
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
</template>

<script lang="ts">
export default {
  data() {
    return {
      drawer: true,
      rail: true,
    }
  },
}
</script>