(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[460],{3905:function(e,t,r){"use strict";r.d(t,{Zo:function(){return l},kt:function(){return f}});var n=r(7294);function s(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){s(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,s=function(e,t){if(null==e)return{};var r,n,s={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(s[r]=e[r]);return s}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(s[r]=e[r])}return s}var i=n.createContext({}),p=function(e){var t=n.useContext(i),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},l=function(e){var t=p(e.components);return n.createElement(i.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var r=e.components,s=e.mdxType,o=e.originalType,i=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),u=p(r),f=s,m=u["".concat(i,".").concat(f)]||u[f]||d[f]||o;return r?n.createElement(m,a(a({ref:t},l),{},{components:r})):n.createElement(m,a({ref:t},l))}));function f(e,t){var r=arguments,s=t&&t.mdxType;if("string"==typeof e||s){var o=r.length,a=new Array(o);a[0]=u;var c={};for(var i in t)hasOwnProperty.call(t,i)&&(c[i]=t[i]);c.originalType=e,c.mdxType="string"==typeof e?e:s,a[1]=c;for(var p=2;p<o;p++)a[p]=r[p];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}u.displayName="MDXCreateElement"},6645:function(e,t,r){"use strict";r.r(t),r.d(t,{frontMatter:function(){return a},metadata:function(){return c},toc:function(){return i},default:function(){return l}});var n=r(2122),s=r(9756),o=(r(7294),r(3905)),a={sidebar_label:"dtypes",title:"fido.dtypes.dtypes"},c={unversionedId:"reference/fido/dtypes/dtypes",id:"reference/fido/dtypes/dtypes",isDocsHomePage:!1,title:"fido.dtypes.dtypes",description:"DType Objects",source:"@site/docs/reference/fido/dtypes/dtypes.md",sourceDirName:"reference/fido/dtypes",slug:"/reference/fido/dtypes/dtypes",permalink:"/fido/docs/reference/fido/dtypes/dtypes",editUrl:"https://github.com/hojulian/fido/edit/documentation/docs/docs/reference/fido/dtypes/dtypes.md",version:"current",sidebar_label:"dtypes",frontMatter:{sidebar_label:"dtypes",title:"fido.dtypes.dtypes"},sidebar:"apiSidebar",previous:{title:"API Reference",permalink:"/fido/docs/reference/api"},next:{title:"fido.robot.robot",permalink:"/fido/docs/reference/fido/robot/robot"}},i=[{value:"DType Objects",id:"dtype-objects",children:[]},{value:"Odom Objects",id:"odom-objects",children:[]},{value:"Twist Objects",id:"twist-objects",children:[]},{value:"LaserScan Objects",id:"laserscan-objects",children:[]},{value:"Image Objects",id:"image-objects",children:[]}],p={toc:i};function l(e){var t=e.components,r=(0,s.Z)(e,["components"]);return(0,o.kt)("wrapper",(0,n.Z)({},p,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h2",{id:"dtype-objects"},"DType Objects"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"class DType(Protocol)\n")),(0,o.kt)("p",null,"Represents the type of the element used by sensors and components."),(0,o.kt)("p",null,"It is implemented as a wrapper around common ROS messages."),(0,o.kt)("h2",{id:"odom-objects"},"Odom Objects"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"class Odom(DType)\n")),(0,o.kt)("p",null,"Represents a odometry state."),(0,o.kt)("p",null,"This is equivalent to ROS","'","s nav_msgs/Odometry."),(0,o.kt)("h2",{id:"twist-objects"},"Twist Objects"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"@dataclass(repr=True)\nclass Twist(DType)\n")),(0,o.kt)("p",null,"Represents a twist message."),(0,o.kt)("p",null,"This is equivalent to ROS","'","s geometry_msgs/Twist."),(0,o.kt)("h2",{id:"laserscan-objects"},"LaserScan Objects"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"@dataclass(frozen=True, repr=True)\nclass LaserScan(DType)\n")),(0,o.kt)("p",null,"Represents a laser scan in 360 degrees."),(0,o.kt)("p",null,"This is equivalent to ROS","'","s sensor_msgs/LaserScan."),(0,o.kt)("h2",{id:"image-objects"},"Image Objects"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"@dataclass(frozen=True, repr=True)\nclass Image(DType)\n")),(0,o.kt)("p",null,"Represents an image."),(0,o.kt)("p",null,"This is equivalent to ROS","'","s sensor_msgs/Image."))}l.isMDXComponent=!0}}]);