<template>
  <div>
    <v-col>
      <v-row class="justify-center redMilk-50">
        <div class="text-h1 mt-2 font-weight-bold">{{Number(PatientStatistics.total_case).toLocaleString()}}</div>
      </v-row>
      <v-row class="justify-end redMilk-50">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold">ราย</div>
      </v-row>
      <v-row class="red">
        <v-col cols="8">
          <div class="text-h6">ติดเชื้อในประเทศ</div>
        </v-col>
        <v-col cols="4" align="right">
          <div class="text-h4 font-weight-bold">{{Number(PatientStatistics.total_case_domestic).toLocaleString()}}</div>
        </v-col>
      </v-row>
      <v-row class="redMilk-100">
        <v-col cols="8">
          <div class="text-h6">ตรวจคัดกรองเชิงรุก</div>
        </v-col>
        <v-col cols="4" align="right">
          <div class="text-h4 font-weight-bold">{{Number(PatientStatistics.total_case_check_point).toLocaleString()}}</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="pa-6 redMilk-25">
          <v-row class="justify-center">
            <div class="text-h6">ผู้เดินทางจากต่างประเทศ</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(PatientStatistics.total_case_from_foreign).toLocaleString()}}</div>
          </v-row>
        </v-col>
        <v-col class="pa-6 redMilk-75" style="height:8rem;">
          <v-row class="justify-center">
            <div class="text-h6">สถานที่กักกันที่รัฐจัดให้</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(PatientStatistics.total_case_in_q).toLocaleString()}}</div>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </div>
</template>

<script>
export default {
  name: 'accumulate',
  data: () => ({
  }),
  props: {
    PatientStatistics: {
      type: Object
    }
  }
}
</script>

<style scoped>
.redMilk-25{
    background-color: rgb(233, 147, 126);
    color: #ffffff;
}
.redMilk-50{
    background-color: rgb(235,122,111);
    color: #ffffff;
}
.redMilk-75{
    background-color: rgb(161,78,77);
    color: #ffffff;
}
.redMilk-100{
    background-color: rgb(147,52,37);
    color: #ffffff;
}
.red{
    background-color: rgb(233,70,42);
    color: #ffffff;
}
</style>
