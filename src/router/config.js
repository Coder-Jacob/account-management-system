import TabsView from '@/layouts/tabs/TabsView'
import BlankView from '@/layouts/BlankView'
// import PageView from '@/layouts/PageView'

// 路由配置
const options = {
  routes: [
    {
      path: '/login',
      name: '登录页',
      component: () => import('@/pages/login')
    },
    {
      path: '*',
      name: '404',
      component: () => import('@/pages/exception/404'),
    },
    {
      path: '/403',
      name: '403',
      component: () => import('@/pages/exception/403'),
    },
    {
      path: '/',
      name: '首页',
      component: TabsView,
      // redirect: '/login',
      redirect:'/home/dashboard',
      children: [
        {
          path: 'home',
          name: '首页',
          meta: {
            icon: 'home'
          },
          component: BlankView,
          children: [
            {
              path: 'dashboard',
              name: '控制台',
              component: () => import('@/pages/dashboard'),
            }
          ],
        },
        {
          path: 'parent1',
          name: '菜单管理',
          meta: {
            icon: 'dashboard',
          },
          component: BlankView,
          children: [
            {
              path: 'demo1',
              name: '演示页面1',
              component: () => import('@/pages/demo'),
            }
          ]
        },
        {
          path: 'account',
          name: '账号管理',
          meta: {
            icon: 'form'
          },
          component: BlankView,
          children: [
            {
              path: 'server',
              name: '服务器',
              component: () => import('@/pages/accounts/Service'),
            },
            {
              path: 'baota',
              name: '宝塔',
              component: () => import('@/pages/accounts/Baota'),
            },
            {
              path: 'develop',
              name: '开发',
              component: () => import('@/pages/accounts/Develop'),
            },
            {
              path: 'everyday',
              name: '日常',
              component: () => import('@/pages/accounts/Everyday'),
            }
          ]
        },
        {
          path: 'exception',
          name: '异常页',
          meta: {
            icon: 'warning',
          },
          component: BlankView,
          children: [
            {
              path: '404',
              name: 'Exp404',
              component: () => import('@/pages/exception/404')
            },
            {
              path: '403',
              name: 'Exp403',
              component: () => import('@/pages/exception/403')
            },
            {
              path: '500',
              name: 'Exp500',
              component: () => import('@/pages/exception/500')
            }
          ]
        },
        {
          name: '验权页面',
          path: 'auth/demo',
          meta: {
            icon: 'file-ppt',
            authority: {
              permission: 'form',
              role: 'manager'
            },
            component: () => import('@/pages/demo')
          }
        }
      ]
    }
  ]
}

export default options
