import { getAssetFromKV } from '@cloudflare/kv-asset-handler'

async function handleEvent(event) {
  try {
    const url = new URL(event.request.url)
    
    // 特殊处理sitemap.xml
    if (url.pathname === '/sitemap.xml') {
      const asset = await getAssetFromKV(event, {
        cacheControl: {
          browserTTL: 3600,
          edgeTTL: 3600,
        },
      })
      
      // 返回正确的XML Content-Type
      return new Response(asset.body, {
        headers: {
          'Content-Type': 'application/xml; charset=utf-8',
          'Cache-Control': 'public, max-age=3600',
          'X-Content-Type-Options': 'nosniff',
        },
        status: 200,
      })
    }
    
    // 处理其他文件
    return await getAssetFromKV(event, {
      cacheControl: {
        browserTTL: 3600,
        edgeTTL: 3600,
      },
    })
  } catch (e) {
    let pathname = new URL(event.request.url).pathname
    return new Response(`"${pathname}" not found`, {
      status: 404,
      statusText: 'not found',
    })
  }
}

addEventListener('fetch', event => {
  event.respondWith(handleEvent(event))
})
