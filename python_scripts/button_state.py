inputEntity = data.get('entity_id')
inputStateObject = hass.states.get(inputEntity)
inputState = inputStateObject.state


newState = data.get('state')
if newState is not None:
    inputState = newState
    

hass.states.set(inputEntity, inputState)