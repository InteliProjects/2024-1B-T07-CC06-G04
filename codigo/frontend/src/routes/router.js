import { createBrowserRouter } from "react-router-dom";
import History from "../pages/HistoryPage";
import Homepage from "../pages/Homepage";
import Main from "../pages/Main";

const AppRoutes = createBrowserRouter([
  {
    path: "/",
    element: <Homepage />,
  },
  {
    path: "/history",
    element: <History />,
  },
  {
    path: "/main/:task_id",
    element: <Main />,
  },
  {
    path:"/main",
    element: <Main/>
  }
]);
  
export default AppRoutes;
