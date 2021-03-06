import React from "react";
import Header from "./header";
import { CardBody, Card, Col, Row, CardText, Button } from "reactstrap";
import { StateContext } from "../App";
import placeholder from "../images/placeholder.png";
import Tips from "./tips";
import { getProfileData } from "./helpers";
import { useHistory } from "react-router-dom";
import EditProfileModal from './editProfileModal'
import { toggleModal } from "./actions";

const Profile = (props) => {
  const { state, dispatch } = React.useContext(StateContext);
  const key = window.localStorage.getItem("key");
  const history = useHistory();

  const openModal = () => {
    dispatch(toggleModal());
  };
  React.useEffect(() => {
    if (history.action === "PUSH" || history.action === "POP") {
      getProfileData(key, dispatch);
    }
  }, [key, dispatch, history]);

  return (
    <div style={{ backgroundColor: "#4a5066", height: "1000px" }}>
      <Header />
      <h1 className="profile">Your Profile</h1>
      <div></div>
      <Row
        style={{
          width: "60em",
          marginTop: "2.5em",
          marginLeft: "auto",
          marginRight: "auto",
        }}
      >
        <Col col-6="true">
          <Card
            style={{
              width: "25em",
              boxShadow: "5px 10px 2px #888888",
            }}
          >
            <CardBody>
              <Row style={{ textAlign: "center" }}>
                <img
                  alt="profilepic"
                  src={placeholder}
                  style={{
                    width: "10em",
                    paddingRight: "1em",
                    fontFamily: "Montserrat",
                  }}
                />
              </Row>
              {state.profile &&
                state.profile.map((value, index) => (
                  <React.Fragment key={index}>
                    <CardText>Name:{value.displayname}</CardText>
                    <CardText>Age:{value.age}</CardText>
                    <CardText>Gender:{value.gender}</CardText>
                    <CardText>
                      Sexual Preference:{value.sexual_preference}
                    </CardText>
                    <CardText>Bio:{value.bio}</CardText>
                  </React.Fragment>
                ))}
            </CardBody>
          </Card>
         
          <Button size="lg" style={{ marginTop: "2em" }} onClick={() => openModal()}>Edit Profile</Button>
          <EditProfileModal show={state.modal} onHide={() => openModal()} />
        </Col>
        <Col col-6="true">
          <Tips />
        </Col>
      </Row>
    </div>
  );
};

export default Profile;
