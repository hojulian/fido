(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[3046],{3905:function(e,t,r){"use strict";r.d(t,{Zo:function(){return d},kt:function(){return p}});var o=r(7294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,o,n=function(e,t){if(null==e)return{};var r,o,n={},a=Object.keys(e);for(o=0;o<a.length;o++)r=a[o],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(o=0;o<a.length;o++)r=a[o],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var l=o.createContext({}),s=function(e){var t=o.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):c(c({},t),e)),r},d=function(e){var t=s(e.components);return o.createElement(l.Provider,{value:t},e.children)},f={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},u=o.forwardRef((function(e,t){var r=e.components,n=e.mdxType,a=e.originalType,l=e.parentName,d=i(e,["components","mdxType","originalType","parentName"]),u=s(r),p=n,m=u["".concat(l,".").concat(p)]||u[p]||f[p]||a;return r?o.createElement(m,c(c({ref:t},d),{},{components:r})):o.createElement(m,c({ref:t},d))}));function p(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var a=r.length,c=new Array(a);c[0]=u;var i={};for(var l in t)hasOwnProperty.call(t,l)&&(i[l]=t[l]);i.originalType=e,i.mdxType="string"==typeof e?e:n,c[1]=i;for(var s=2;s<a;s++)c[s]=r[s];return o.createElement.apply(null,c)}return o.createElement.apply(null,r)}u.displayName="MDXCreateElement"},6202:function(e,t,r){"use strict";r.r(t),r.d(t,{frontMatter:function(){return c},metadata:function(){return i},toc:function(){return l},default:function(){return d}});var o=r(2122),n=r(9756),a=(r(7294),r(3905)),c={sidebar_label:"stack",title:"fido.robot.model.stack"},i={unversionedId:"reference/fido/robot/model/stack",id:"reference/fido/robot/model/stack",isDocsHomePage:!1,title:"fido.robot.model.stack",description:"Stack Objects",source:"@site/docs/reference/fido/robot/model/stack.md",sourceDirName:"reference/fido/robot/model",slug:"/reference/fido/robot/model/stack",permalink:"/fido/docs/reference/fido/robot/model/stack",editUrl:"https://github.com/hojulian/fido/edit/documentation/docs/docs/reference/fido/robot/model/stack.md",version:"current",sidebar_label:"stack",frontMatter:{sidebar_label:"stack",title:"fido.robot.model.stack"},sidebar:"apiSidebar",previous:{title:"fido.robot.model.model",permalink:"/fido/docs/reference/fido/robot/model/model"},next:{title:"fido.robot.robot",permalink:"/fido/docs/reference/fido/robot/robot"}},l=[{value:"Stack Objects",id:"stack-objects",children:[]}],s={toc:l};function d(e){var t=e.components,r=(0,n.Z)(e,["components"]);return(0,a.kt)("wrapper",(0,o.Z)({},s,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h2",{id:"stack-objects"},"Stack Objects"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"class Stack(object)\n")),(0,a.kt)("p",null,"Represents a physical robot in stack form."),(0,a.kt)("p",null,"Stack is used for building a ",(0,a.kt)("inlineCode",{parentName:"p"},"fido.robot.model.Model"),". Intuitively,\nin Fido, a robot model is represented in a stack of layers, from\nbottom to top (think of it like a sandwich). Each layer has a\ncertain size, and can attach various wheels and components. To form\na stack, each layer is rigidly joined vertically."),(0,a.kt)("h4",{id:"model"},"model"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"}," | model()\n")),(0,a.kt)("p",null,"Converts the stack representation into a ",(0,a.kt)("inlineCode",{parentName:"p"},"fido.robot.model.Model"),"."))}d.isMDXComponent=!0}}]);