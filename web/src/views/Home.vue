<template>
  <div class="home">
    <v-row>
      <v-col cols="4">
        <v-img :src="lgImg" width="15%" class="mt-4 ml-4"></v-img>
      </v-col>
      <v-col cols="8" style="text-align:right;">
        <p class="mr-2" style="font-size:50pt;color:#fff;">สถานการณ์ covid-19 ในประเทศไทย</p>
        <p class="mt-n6 mr-2" style="font-size:30pt;color:#fff;">ข้อมูลวันที่ {{data.DataDate}}</p>
        <p class="mt-n2 mr-2" style="font-size:15pt;color:#fff;">กรมควบคุมโรค กระทรวงสาธารณสุข</p>
      </v-col>
    </v-row>
    <v-row class="pa-4">
      <v-col cols="8" style="margin-top:-3%;">
        <v-row>
          <v-col cols="6">
            <h1 class="color-wh1">ผู้ป่วยรายใหม่ในวันนี้</h1>
            <patientNow :PatientToDay='PatientToDay' />
          </v-col>
          <v-col cols="6">
            <h1 class="color-wh1">ผู้ป่วยยืนยันสะสม</h1>
            <accumulate :PatientStatistics='PatientStatistics'/>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            <h1 class="color-h1">หายป่วยแล้ว</h1>
            <GetWell :ReceivedTreatment='ReceivedTreatment'/>
          </v-col>
          <v-col cols="6">
            <h1 class="color-h1">เสียชีวิต</h1>
            <Died :DiedSatatistics='DiedSatatistics'/>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="4" align-self="center">
        <region :RegionStatistics='RegionStatistics'/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import patientNow from '@/components/patientNow.vue'
import accumulate from '@/components/accumulate.vue'
import GetWell from '../components/getWell.vue'
import Died from '../components/died.vue'
import region from '../components/region.vue'

export default {
  name: 'Home',
  components: {
    patientNow,
    accumulate,
    GetWell,
    Died,
    region
  },
  data: () => ({
    data: {},
    DiedSatatistics: {},
    PatientStatistics: {},
    PatientToDay: {},
    ReceivedTreatment: {},
    RegionStatistics: {},
    lgImg: require('@/assets/lg.png')
  }),
  created () {
    this.getData()
  },
  methods: {
    async getData () {
      try {
        await this.axios.get('http://10.99.150.187:8000/api/v1/covid').then(res => {
          this.data = res.data
          this.DiedSatatistics = res.data.DiedSatatistics
          this.PatientStatistics = res.data.PatientStatistics
          this.PatientToDay = res.data.PatientToDay
          this.ReceivedTreatment = res.data.ReceivedTreatment
          this.RegionStatistics = res.data.RegionStatistics
          console.log('data', this.data)
        })
      } catch (err) {

      }
    }
  }
}
</script>

<style scoped>
/* .home{
  background-color: brown;
} */
.color-h1{
  color: #3b3b3b;
}
.color-wh1{
  color: #ffffff;
}
.bg-img-main{
  /* position: absolute; */
  left: 0px;
  top: 0px;
  /* z-index: 0; */
}
</style>
