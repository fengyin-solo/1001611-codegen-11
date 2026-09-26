import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Project = () => import('@/views/project/index.vue')
const Drilling = () => import('@/views/drilling/index.vue')
const Core = () => import('@/views/core/index.vue')
const Geophysics = () => import('@/views/geophysics/index.vue')
const Geochem = () => import('@/views/geochem/index.vue')
const Surveying = () => import('@/views/surveying/index.vue')
const Trenching = () => import('@/views/trenching/index.vue')
const Sample = () => import('@/views/sample/index.vue')
const Labtest = () => import('@/views/labtest/index.vue')
const Report = () => import('@/views/report/index.vue')
const SafetyGeo = () => import('@/views/safety_geo/index.vue')
const PermitGeo = () => import('@/views/permit_geo/index.vue')
const Camp = () => import('@/views/camp/index.vue')
const TransportGeo = () => import('@/views/transport_geo/index.vue')
const EquipmentGeo = () => import('@/views/equipment_geo/index.vue')
const PersonnelGeo = () => import('@/views/personnel_geo/index.vue')
const BudgetGeo = () => import('@/views/budget_geo/index.vue')
const ReviewGeo = () => import('@/views/review_geo/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/project', name: 'project', component: Project },
    { path: '/drilling', name: 'drilling', component: Drilling },
    { path: '/core', name: 'core', component: Core },
    { path: '/geophysics', name: 'geophysics', component: Geophysics },
    { path: '/geochem', name: 'geochem', component: Geochem },
    { path: '/surveying', name: 'surveying', component: Surveying },
    { path: '/trenching', name: 'trenching', component: Trenching },
    { path: '/sample', name: 'sample', component: Sample },
    { path: '/labtest', name: 'labtest', component: Labtest },
    { path: '/report', name: 'report', component: Report },
    { path: '/safety_geo', name: 'safety_geo', component: SafetyGeo },
    { path: '/permit_geo', name: 'permit_geo', component: PermitGeo },
    { path: '/camp', name: 'camp', component: Camp },
    { path: '/transport_geo', name: 'transport_geo', component: TransportGeo },
    { path: '/equipment_geo', name: 'equipment_geo', component: EquipmentGeo },
    { path: '/personnel_geo', name: 'personnel_geo', component: PersonnelGeo },
    { path: '/budget_geo', name: 'budget_geo', component: BudgetGeo },
    { path: '/review_geo', name: 'review_geo', component: ReviewGeo },
  ],
})

export default router
