<template>
  <v-app>
    <v-main>
      <SideBar />
      <ContentTest />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import SideBar from '@/components/SideBar.vue';
import ContentTest from '@/components/ContentTest.vue';
</script>