<template>
  <div>
    <v-col class="yellow1 pa-6">
        <div class="mt-2 font-weight-bold font-22">จำนวนผู้ป่วยยืนยันจำแนกตามพื้นที่รักษา(ราย)</div>
    </v-col>
    <v-col class="grey1 mt-4">
      <v-row class="justify-start">
        <div class="mt-2 ml-2 font-grey1">กรุงเทพฯ และนนทบุรี</div>
      </v-row>
      <v-row class="justify-end">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold font-red">{{Number(RegionStatistics.bkk_and_nearby).toLocaleString()}}</div>
      </v-row>
    </v-col>
    <v-col class="grey1 mt-4">
      <v-row class="justify-start">
        <div class="mt-2 ml-2 font-grey1">ภาคเหนือ</div>
      </v-row>
      <v-row class="justify-end">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold font-grey2">{{Number(RegionStatistics.north_region).toLocaleString()}}</div>
      </v-row>
    </v-col>
    <v-col class="grey1 mt-4">
      <v-row class="justify-start">
        <div class="mt-2 ml-2 font-grey1">ภาคกลาง</div>
      </v-row>
      <v-row class="justify-end">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold font-red">{{Number(RegionStatistics.central_region).toLocaleString()}}</div>
      </v-row>
    </v-col>
    <v-col class="grey1 mt-4">
      <v-row class="justify-start">
        <div class="mt-2 ml-2 font-grey1">ภาคตะวันออกเฉียงเหนือ</div>
      </v-row>
      <v-row class="justify-end">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold font-grey2">{{Number(RegionStatistics.esan_region).toLocaleString()}}</div>
      </v-row>
    </v-col>
    <v-col class="grey1 mt-4">
      <v-row class="justify-start">
        <div class="mt-2 ml-2 font-grey1">ภาคใต้</div>
      </v-row>
      <v-row class="justify-end">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold font-red">{{Number(RegionStatistics.south).toLocaleString()}}</div>
      </v-row>
    </v-col>
  </div>
</template>

<script>
export default {
  name: 'region',
  data: () => ({
  }),
  props: {
    RegionStatistics: {
      type: Object
    }
  }
}
</script>

<style scoped>
.grey1{
    background-color: rgba(214, 215, 218, 0.7);
}
.font-grey1{
    color: #585858;
    font-size: 20pt;
}
.font-grey2{
    color: #707070;
}
.font-red{
    color: #d85151;
}
.font-22{
    font-size: 22pt;
}
.yellow1{
    background-color: rgb(232, 182, 62);
    color: #ffffff;
}
</style>
