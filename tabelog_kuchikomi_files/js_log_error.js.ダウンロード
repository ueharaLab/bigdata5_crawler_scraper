var JsLogger = {};

(function(){
  var ignorePatterns = [
    {
      line: 6,
      message: 'Uncaught TypeError: Cannot read property \'length\' of undefined'
    },
    {
      line: 353,
      message: 'TypeError: \'null\' is not an object'
    },
    {
      line: 92,
      message: 'TypeError: \'null\' is not an object'
    },
    {
      javascript: 'jquery.easing.1.3.js',
      caller: 'return jQuery.easing[jQuery.easing.def]'
    },
    {
      line: 47,
      message: 'Uncaught TypeError: Cannot call method \'removeEventListener\' of undefined'
    },
    {
      line: 35,
      message: 'Uncaught TypeError: Object #<Text> has no method \'getBoundingClientRect\''
    }
  ];
  function isReproducibleError(ua, url, wkunknown, line, message, caller){
    if(/MSIE\s6|MSIE\s7|MSIE\s5/.test(ua) || /extension/.test(url) || (wkunknown !== 'true' && !/\.js/.test(url) && line <= 3)){
      return false;
    }else{
      var ignoreCompare = {
        line: line,
        message: message,
        javascript: url,
        caller: caller
      };
      for(var i = 0; i < ignorePatterns.length; i++){
        var ignoreMatched = true;
        for (var attr in ignorePatterns[i]){
          if(typeof ignoreCompare[attr] === 'number'){
            if(ignoreCompare[attr] !== ignorePatterns[i][attr]){
              ignoreMatched = false;
              break;
            }
          }else if(typeof ignoreCompare[attr] === 'string'){
            if(ignoreCompare[attr].indexOf(ignorePatterns[i][attr], 0) < 0){
              ignoreMatched = false;
              break;
            }
          }
        }
        if(ignoreMatched){
          return false;
        }
      }
      return true;
    }
  }
  function isAddonError(message, caller){
    var msgExp = /interstitial|originalCreateNotification|youtube|SleipnirMobile/;
    var callExp = /MyIPhoneApp|youtube/;
    if(msgExp.test(message) || callExp.test(caller)){
      return true;
    }else{
      return false;
    }
  }
  JsLogger.error = function(message, url, line, caller){
    var wkunknown = '';
    if(!/tabelog/.test(url)){
      if(/AppleWebKit/.test(navigator.userAgent) && /Mobile|Android/.test(navigator.userAgent)){
        if (Math.random() * 10 >= 9){
          message = 'Unknown Error that was thrown from Smartphone Webkit, Please check your browser\'s console';
          wkunknown = 'true';
        }else{
          return;
        }
      }else{
        return;
      }
    }
    var host = location.href.match(/:\/\/(.+?)\//)[1];
    if(!/tabelog/.test(host) || !isReproducibleError(navigator.userAgent, url, wkunknown, line, message, caller) || isAddonError(message, caller)){
      return;
    }
    var pageUrl = location.href;
    var domain = pageUrl.match(/:\/\/(.*?)\./)[1];
    if(domain === 'tabelog' || domain === 's' || /d\d+/.test(domain) || /\/smartphone\//.test(pageUrl)){
      if(Math.random() * 50 < 49){
       return;
      }
    }

    var hostForLogSend;
    if(/https/.test(location.protocol)){
      hostForLogSend = 'https://ssl.tabelog.com';
    }else{
      hostForLogSend = 'https://tabelog.com';
    }
    var param = 'page_url=' + encodeURIComponent(pageUrl) + '&message=' + encodeURIComponent(message) + '&url=' + encodeURIComponent(url) + '&line=' + line;
    param = param + '&caller=' + encodeURIComponent(caller);
    new Image().src = hostForLogSend + '/js_log/error?' + param + '&c=' + Math.round(new Date().getTime() / 1000);

  };
})();

window.onerror = function(message, url, line){
  var caller = String(arguments.callee.caller).slice(0, 200);
  JsLogger.error(message, url, line, caller);
};

