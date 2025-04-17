// 等待文檔加載完成
document.addEventListener("DOMContentLoaded", () => {
    // 導航欄滾動效果
    const navbar = document.querySelector(".navbar")
  
    if (navbar) {
      window.addEventListener("scroll", () => {
        if (window.scrollY > 50) {
          navbar.classList.add("navbar-scrolled", "shadow-sm")
        } else {
          navbar.classList.remove("navbar-scrolled", "shadow-sm")
        }
      })
    }
  
    // 平滑滾動到錨點
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        const href = this.getAttribute("href")
  
        if (href !== "#") {
          e.preventDefault()
  
          const targetElement = document.querySelector(href)
          if (targetElement) {
            targetElement.scrollIntoView({
              behavior: "smooth",
            })
          }
        }
      })
    })
  
    // 初始化工具提示
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl))
  })
  