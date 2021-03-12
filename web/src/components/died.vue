<template>
  <div>
    <v-col>
      <v-row class="justify-center grey-1">
        <div class="text-h1 mt-12 font-weight-bold">{{Number(DiedSatatistics.total_died).toLocaleString()}}</div>
      </v-row>
      <v-row class="justify-end grey-1">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold">ราย</div>
      </v-row>
      <v-row>
        <v-col class="pa-6 grey-2">
          <v-row class="justify-center">
            <div class="text-h6">new case เพิ่มขึ้น</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(DiedSatatistics.case_new_died).toLocaleString()}}</div>
          </v-row>
        </v-col>
        <v-col class="pa-6 grey-3">
          <v-row class="justify-center">
            <div class="text-h6">ร้อยละ</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(DiedSatatistics.percentage).toLocaleString()}}</div>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </div>
</template>

<script>
export default {
  name: 'died',
  data: () => ({
  }),
  props: {
    DiedSatatistics: {
      type: Object
    }
  }
}
</script>

<style scoped>
.grey-1{
    background-color: rgb(96, 96, 96);
    color: #ffffff;
}
.grey-2{
    background-color: rgb(84,86,83);
    color: #ffffff;
}
.grey-3{
    background-color: rgb(109,111,108);
    color: #ffffff;
}
</style>
