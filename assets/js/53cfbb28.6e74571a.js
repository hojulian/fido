(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[6072],{3905:function(e,t,o){"use strict";o.d(t,{Zo:function(){return p},kt:function(){return f}});var r=o(7294);function n(e,t,o){return t in e?Object.defineProperty(e,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[t]=o,e}function a(e,t){var o=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),o.push.apply(o,r)}return o}function l(e){for(var t=1;t<arguments.length;t++){var o=null!=arguments[t]?arguments[t]:{};t%2?a(Object(o),!0).forEach((function(t){n(e,t,o[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(o)):a(Object(o)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(o,t))}))}return e}function i(e,t){if(null==e)return{};var o,r,n=function(e,t){if(null==e)return{};var o,r,n={},a=Object.keys(e);for(r=0;r<a.length;r++)o=a[r],t.indexOf(o)>=0||(n[o]=e[o]);return n}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)o=a[r],t.indexOf(o)>=0||Object.prototype.propertyIsEnumerable.call(e,o)&&(n[o]=e[o])}return n}var s=r.createContext({}),c=function(e){var t=r.useContext(s),o=t;return e&&(o="function"==typeof e?e(t):l(l({},t),e)),o},p=function(e){var t=c(e.components);return r.createElement(s.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},u=r.forwardRef((function(e,t){var o=e.components,n=e.mdxType,a=e.originalType,s=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),u=c(o),f=n,b=u["".concat(s,".").concat(f)]||u[f]||d[f]||a;return o?r.createElement(b,l(l({ref:t},p),{},{components:o})):r.createElement(b,l({ref:t},p))}));function f(e,t){var o=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var a=o.length,l=new Array(a);l[0]=u;var i={};for(var s in t)hasOwnProperty.call(t,s)&&(i[s]=t[s]);i.originalType=e,i.mdxType="string"==typeof e?e:n,l[1]=i;for(var c=2;c<a;c++)l[c]=o[c];return r.createElement.apply(null,l)}return r.createElement.apply(null,o)}u.displayName="MDXCreateElement"},7617:function(e,t,o){"use strict";o.r(t),o.d(t,{frontMatter:function(){return l},metadata:function(){return i},toc:function(){return s},default:function(){return p}});var r=o(2122),n=o(9756),a=(o(7294),o(3905)),l={sidebar_label:"robot",title:"fido.robot.robot"},i={unversionedId:"reference/fido/robot/robot",id:"reference/fido/robot/robot",isDocsHomePage:!1,title:"fido.robot.robot",description:"Robot Objects",source:"@site/docs/reference/fido/robot/robot.md",sourceDirName:"reference/fido/robot",slug:"/reference/fido/robot/robot",permalink:"/fido/docs/reference/fido/robot/robot",editUrl:"https://github.com/hojulian/fido/edit/documentation/docs/docs/reference/fido/robot/robot.md",version:"current",sidebar_label:"robot",frontMatter:{sidebar_label:"robot",title:"fido.robot.robot"},sidebar:"apiSidebar",previous:{title:"fido.dtypes.dtypes",permalink:"/fido/docs/reference/fido/dtypes/dtypes"},next:{title:"fido.robot.turtlebot3",permalink:"/fido/docs/reference/fido/robot/turtlebot3"}},s=[{value:"Robot Objects",id:"robot-objects",children:[]}],c={toc:s};function p(e){var t=e.components,o=(0,n.Z)(e,["components"]);return(0,a.kt)("wrapper",(0,r.Z)({},c,o,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h2",{id:"robot-objects"},"Robot Objects"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"class Robot(ABC,  RobotProtocol)\n")),(0,a.kt)("p",null,"Represents a physical or simulated robot."),(0,a.kt)("h4",{id:"add_sensor"},"add","_","sensor"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},' | add_sensor(sensor_cls: Type["Sensor"], sensor_args: Mapping[str, Any] = {}) -> None\n')),(0,a.kt)("p",null,"Add sensor to the robot."),(0,a.kt)("h4",{id:"prepare"},"prepare"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"}," | prepare() -> None\n")),(0,a.kt)("p",null,"Prepare initializes all the sensors in the robot."),(0,a.kt)("h4",{id:"set_world"},"set","_","world"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},' | set_world(world: "World") -> None\n')),(0,a.kt)("p",null,"Set the world to use for this robot."),(0,a.kt)("h4",{id:"move"},"move"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | move(distance: float = 0, duration: float = 0, speed: float = 0) -> None\n")),(0,a.kt)("p",null,"Move the robot at a certain distance at a certain speed or for a\ncertain duration."),(0,a.kt)("p",null,"To move backwards, set speed to negative. If the given speed is\nlarger than the maximum speed, it will be set to the maximum\nspeed."),(0,a.kt)("h4",{id:"rotate"},"rotate"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | rotate(angle: float = 0, duration: float = 0, speed: float = 0) -> None\n")),(0,a.kt)("p",null,"Rotate the robot at a certain angle at a certain speed or for a\ncertain duration."),(0,a.kt)("p",null,"To rotate clockwise, set the speed to positive. To rotate in\nanti-clockwise, set the speed to negative. If the given speed is\nlarger  than the maximum speed, it will be set to the maximum\nspeed."),(0,a.kt)("h4",{id:"stop"},"stop"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | stop(forced: bool = False) -> None\n")),(0,a.kt)("p",null,"Stop the robot."),(0,a.kt)("p",null,"This is a blocking call. It will block execution until the robot\nis gracefully stopped unless ",(0,a.kt)("inlineCode",{parentName:"p"},"forced")," is set to ",(0,a.kt)("inlineCode",{parentName:"p"},"True"),"."),(0,a.kt)("h4",{id:"ros_robot_description"},"ros","_","robot","_","description"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | ros_robot_description() -> str\n")),(0,a.kt)("p",null,"Return the ROS specific robot description."),(0,a.kt)("p",null,"This is mainly used for building the launch file."),(0,a.kt)("h4",{id:"ros_fill_dependency"},"ros","_","fill","_","dependency"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | ros_fill_dependency(installfile: InstallFile) -> None\n")),(0,a.kt)("p",null,"Fill the needed dependency to the given installfile."))}p.isMDXComponent=!0}}]);