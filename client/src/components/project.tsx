import * as React from "react";
import {Button, ButtonToolbar} from "react-bootstrap";
import {LinkContainer} from "react-router-bootstrap";

import {ProjectModel} from "../models/project";


export interface Props {
  project: ProjectModel;
  onDelete: () => void;
}

function Project({project, onDelete}: Props) {
  return (
    <div className="row">
      <div className="col-md-12 project">
        <h4 className="title"><a>{ project.name }</a></h4>
        <div>{ project.description }</div>
        <div className="meta">{ project.createdAt.toLocaleTimeString() }</div>
        <ButtonToolbar className="pull-right">
          <LinkContainer to={`/projects/${project.id}`}><Button>View</Button></LinkContainer>
          <Button bsStyle="danger" className="pull-right" onClick={onDelete}>delete</Button>
        </ButtonToolbar>
      </div>
    </div>
  );
}

export default Project;
