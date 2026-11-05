/* Bilingual copy is local. No external services, tracking, or simulated live state. */
(() => {
  const elements = [...document.querySelectorAll('[data-zh]')];
  elements.forEach(element => { element.dataset.en = element.hasAttribute('data-html') ? element.innerHTML : element.textContent; });
  const button = document.getElementById('language');
  let language = 'en';
  try { language = localStorage.getItem('ride-language') === 'zh' ? 'zh' : 'en'; } catch (_) { /* storage is optional */ }
  function setLanguage(value) {
    language = value;
    document.documentElement.lang = value === 'zh' ? 'zh-CN' : 'en';
    for (const element of elements) {
      const content = value === 'zh' ? element.dataset.zh : element.dataset.en;
      if (element.hasAttribute('data-html')) element.innerHTML = content;
      else element.textContent = content;
    }
    if (button) {
      button.textContent = value === 'zh' ? 'EN' : '中文';
      button.setAttribute('aria-label', value === 'zh' ? 'Switch to English' : '切换为中文');
    }
    try { localStorage.setItem('ride-language', value); } catch (_) { /* storage is optional */ }
  }
  if (button) button.addEventListener('click', () => setLanguage(language === 'en' ? 'zh' : 'en'));
  setLanguage(language);
})();
