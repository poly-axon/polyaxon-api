import {Reducer} from "redux";

import {ProjectAction, actionTypes} from "../actions/project";
import {ProjectModel} from "../models/project";

export const projectsReducer: Reducer<{byIds: {[id: number]: ProjectModel}, ids: number[]}> =
	(state: {byIds: {[id: number]: ProjectModel}, ids: number[]} = {
    byIds: {},
    ids: []
	}, action: ProjectAction) => {

  switch (action.type) {
    case actionTypes.CREATE_PROJECT:
      return {
        ...state,
        byIds: {...state.byIds, [action.project.id] : project},
        ids: [...state.ids, action.project.id]
      };
    case actionTypes.DELETE_PROJECT:
      return {
        ...state,
        byIds: {...state.byIds, [action.projectId] : {...state.byIds[action.projectId], id_deleted:true}},
        ids: state.ids.filter(id => id != action.projectId),
      };
    case actionTypes.UPDATE_PROJECT:
      return {
        ...state,
        byIds: {...state.byIds, [action.project.id]: action.project}
      };
    case actionTypes.RECEIVE_PROJECTS:
      var newState = {...state};
      for (let project of action.projects) {
        if (!newState.ids.includes(project.id)) {
          newState.ids.push(project.id);
        }
        newState.byIds[project.id] = project;
      }
      return newState;
    case actionTypes.RECEIVE_PROJECT:
      var newState = {...state};
      if (!newState.ids.includes(action.project.id)) {
        newState.ids.push(action.project.id);
      }
      newState.byIds[action.project.id] = action.project;
      return newState;
  }
  return state;
};