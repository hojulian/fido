(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[3769],{3905:function(e,t,o){"use strict";o.d(t,{Zo:function(){return s},kt:function(){return m}});var r=o(67294);function n(e,t,o){return t in e?Object.defineProperty(e,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[t]=o,e}function l(e,t){var o=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),o.push.apply(o,r)}return o}function i(e){for(var t=1;t<arguments.length;t++){var o=null!=arguments[t]?arguments[t]:{};t%2?l(Object(o),!0).forEach((function(t){n(e,t,o[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(o)):l(Object(o)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(o,t))}))}return e}function a(e,t){if(null==e)return{};var o,r,n=function(e,t){if(null==e)return{};var o,r,n={},l=Object.keys(e);for(r=0;r<l.length;r++)o=l[r],t.indexOf(o)>=0||(n[o]=e[o]);return n}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(r=0;r<l.length;r++)o=l[r],t.indexOf(o)>=0||Object.prototype.propertyIsEnumerable.call(e,o)&&(n[o]=e[o])}return n}var c=r.createContext({}),p=function(e){var t=r.useContext(c),o=t;return e&&(o="function"==typeof e?e(t):i(i({},t),e)),o},s=function(e){var t=p(e.components);return r.createElement(c.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},u=r.forwardRef((function(e,t){var o=e.components,n=e.mdxType,l=e.originalType,c=e.parentName,s=a(e,["components","mdxType","originalType","parentName"]),u=p(o),m=n,f=u["".concat(c,".").concat(m)]||u[m]||d[m]||l;return o?r.createElement(f,i(i({ref:t},s),{},{components:o})):r.createElement(f,i({ref:t},s))}));function m(e,t){var o=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var l=o.length,i=new Array(l);i[0]=u;var a={};for(var c in t)hasOwnProperty.call(t,c)&&(a[c]=t[c]);a.originalType=e,a.mdxType="string"==typeof e?e:n,i[1]=a;for(var p=2;p<l;p++)i[p]=o[p];return r.createElement.apply(null,i)}return r.createElement.apply(null,o)}u.displayName="MDXCreateElement"},85547:function(e,t,o){"use strict";o.r(t),o.d(t,{frontMatter:function(){return i},metadata:function(){return a},toc:function(){return c},default:function(){return s}});var r=o(22122),n=o(19756),l=(o(67294),o(3905)),i={sidebar_label:"protocol",title:"fido.ros.protocol"},a={unversionedId:"reference/fido/ros/protocol",id:"reference/fido/ros/protocol",isDocsHomePage:!1,title:"fido.ros.protocol",description:"RobotProtocol",source:"@site/docs/reference/fido/ros/protocol.md",sourceDirName:"reference/fido/ros",slug:"/reference/fido/ros/protocol",permalink:"/fido/docs/reference/fido/ros/protocol",editUrl:"https://github.com/hojulian/fido/edit/documentation/docs/docs/reference/fido/ros/protocol.md",version:"current",sidebar_label:"protocol",frontMatter:{sidebar_label:"protocol",title:"fido.ros.protocol"},sidebar:"apiSidebar",previous:{title:"fido.ros.launchfile",permalink:"/fido/docs/reference/fido/ros/launchfile"},next:{title:"fido.ros.utils",permalink:"/fido/docs/reference/fido/ros/utils"}},c=[{value:"RobotProtocol",id:"robotprotocol",children:[{value:"connect",id:"connect",children:[]},{value:"ros_robot_description",id:"ros_robot_description",children:[]},{value:"ros_fill_dependency",id:"ros_fill_dependency",children:[]},{value:"ros",id:"ros",children:[]}]},{value:"WorldProtocol",id:"worldprotocol",children:[{value:"ros",id:"ros-1",children:[]}]},{value:"SimulatorProtocol",id:"simulatorprotocol",children:[{value:"ros",id:"ros-2",children:[]}]}],p={toc:c};function s(e){var t=e.components,o=(0,n.Z)(e,["components"]);return(0,l.kt)("wrapper",(0,r.Z)({},p,o,{components:t,mdxType:"MDXLayout"}),(0,l.kt)("h2",{id:"robotprotocol"},"RobotProtocol"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},"class RobotProtocol(Protocol)\n")),(0,l.kt)("p",null,"RobotProtocol is implemented by a robot that is ROS compatible."),(0,l.kt)("h3",{id:"connect"},"connect"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | def connect(host: str, port: int) -> None\n")),(0,l.kt)("p",null,"Connect to the robot via ROS bridge."),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"host")," ",(0,l.kt)("em",{parentName:"li"},"str")," - Name or IP address of the ROS bridge host, e.g. ",(0,l.kt)("inlineCode",{parentName:"li"},"127.0.0.1"),"."),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"port")," ",(0,l.kt)("em",{parentName:"li"},"int")," - ROS bridge port, e.g. ",(0,l.kt)("inlineCode",{parentName:"li"},"9090"),".")),(0,l.kt)("h3",{id:"ros_robot_description"},"ros","_","robot","_","description"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | def ros_robot_description() -> str\n")),(0,l.kt)("p",null,"Return the ROS specific robot description."),(0,l.kt)("p",null,"This is mainly used for building the launch file. E.g.\n",(0,l.kt)("inlineCode",{parentName:"p"},"robot_description/urdf/model.urdf"),"."),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Returns"),":"),(0,l.kt)("p",null,"  The robot_description used by the launch file."),(0,l.kt)("h3",{id:"ros_fill_dependency"},"ros","_","fill","_","dependency"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | def ros_fill_dependency(installfile: InstallFile) -> None\n")),(0,l.kt)("p",null,"Fill the needed dependencies to the given installfile."),(0,l.kt)("p",null,"E.g."),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},'installfile.git(\n    "src/turtlebot3",\n    "https://github.com/ROBOTIS-GIT/turtlebot3.git",\n    "master",\n)`\n')),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"installfile")," ",(0,l.kt)("em",{parentName:"li"},"InstallFile")," - InstallFile for filling dependencies.")),(0,l.kt)("h3",{id:"ros"},"ros"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},' | @abstractmethod\n | def ros() -> "Ros"\n')),(0,l.kt)("p",null,"Return internal ROS client."),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Returns"),":"),(0,l.kt)("p",null,"  The ROS client."),(0,l.kt)("h2",{id:"worldprotocol"},"WorldProtocol"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},"class WorldProtocol(Protocol)\n")),(0,l.kt)("p",null,"WorldProtocol is implemented by a world that is ROS compatible."),(0,l.kt)("h3",{id:"ros-1"},"ros"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},' | @abstractmethod\n | def ros() -> "Ros"\n')),(0,l.kt)("p",null,"Return internal ROS client."),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Returns"),":"),(0,l.kt)("p",null,"  The ROS client."),(0,l.kt)("h2",{id:"simulatorprotocol"},"SimulatorProtocol"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},"class SimulatorProtocol(Protocol)\n")),(0,l.kt)("p",null,"SimulatorProtocol is implemented by a simulator that is ROS compatible."),(0,l.kt)("h3",{id:"ros-2"},"ros"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},' | @abstractmethod\n | def ros() -> "Ros"\n')),(0,l.kt)("p",null,"Return internal ROS client."),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Returns"),":"),(0,l.kt)("p",null,"  The ROS client."))}s.isMDXComponent=!0}}]);