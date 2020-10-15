import React from "react";
import { Home } from "./components/landingpage";
import PenPal from "./components/penpal";
import Profile from "./components/profile";
// import Auth from "./components/loginSignup";
import Main from "./components/main";
import Survey from "./components/survey";
import { useLocation } from "react-router-dom";
import { routeDispatcher } from "./components/helpers";
import NotFound from "./components/notfound";

const Routes = () => {
  let path = useLocation();

  let {pathname}=path
  const loggedIn = window.localStorage.getItem("key");
  
  // console.log(pathname);

  // const logOutMatch = useRouteMatch({ path: "/logout/", exact: true });

  let routes = [];

  let urls = {
    PenPal: { path: /^\/messages\//, PenPal },
    Home: { path: /^\/home\//, Home },
    Survey: { path: /^\/survey\/$/, Survey },
    Profile: {
      path: /^\/profile\//,
      Profile,
    },
    Main: { path: /^\/$|\/logout\//, Main },
  };

  for (const key in urls) {
    // console.log(urls[key][key]);
    // console.log(urls[key].path);
    // console.log(urls[key].path.test(pathname));

    if (urls[key].path.test(pathname)) {
      routes = [
        ...routes,
        {
          match: urls[key].path.test(pathname),
          component: urls[key][key],
        },
      ];
      return loggedIn ? routeDispatcher(routes) : <Main />;
    }
  }

  routes = [{ match: true, component: NotFound }];

  return routeDispatcher(routes);
  // return routeDispatcher(routes);
};

export default Routes;
