(this["webpackJsonpmost-subscribed-you-tube-music-channels"]=this["webpackJsonpmost-subscribed-you-tube-music-channels"]||[]).push([[53],{149:function(t,e,n){"use strict";n.r(e),n.d(e,"KEYBOARD_DID_CLOSE",(function(){return o})),n.d(e,"KEYBOARD_DID_OPEN",(function(){return i})),n.d(e,"copyVisualViewport",(function(){return l})),n.d(e,"keyboardDidClose",(function(){return g})),n.d(e,"keyboardDidOpen",(function(){return p})),n.d(e,"keyboardDidResize",(function(){return b})),n.d(e,"resetKeyboardAssist",(function(){return d})),n.d(e,"setKeyboardClose",(function(){return h})),n.d(e,"setKeyboardOpen",(function(){return f})),n.d(e,"startKeyboardAssist",(function(){return a})),n.d(e,"trackViewportChanges",(function(){return v}));var i="ionKeyboardDidShow",o="ionKeyboardDidHide",r={},u={},s=!1,d=function(){r={},u={},s=!1},a=function(t){c(t),t.visualViewport&&(u=l(t.visualViewport),t.visualViewport.onresize=function(){v(t),p()||b(t)?f(t):g(t)&&h(t)})},c=function(t){t.addEventListener("keyboardDidShow",(function(e){return f(t,e)})),t.addEventListener("keyboardDidHide",(function(){return h(t)}))},f=function(t,e){w(t,e),s=!0},h=function(t){y(t),s=!1},p=function(){var t=(r.height-u.height)*u.scale;return!s&&r.width===u.width&&t>150},b=function(t){return s&&!g(t)},g=function(t){return s&&u.height===t.innerHeight},w=function(t,e){var n=e?e.keyboardHeight:t.innerHeight-u.height,o=new CustomEvent(i,{detail:{keyboardHeight:n}});t.dispatchEvent(o)},y=function(t){var e=new CustomEvent(o);t.dispatchEvent(e)},v=function(t){r=Object.assign({},u),u=l(t.visualViewport)},l=function(t){return{width:Math.round(t.width),height:Math.round(t.height),offsetTop:t.offsetTop,offsetLeft:t.offsetLeft,pageTop:t.pageTop,pageLeft:t.pageLeft,scale:t.scale}}}}]);
//# sourceMappingURL=53.fe4287be.chunk.js.map