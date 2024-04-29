import React from 'react'

const LetterCard = ({id, tamil, phonetic, description, sound, type}) => {
  return (
    <div>
        <h1>{tamil}</h1>
        <p>{phonetic}</p>
        <p>{description}</p>
        {/* <audio src={sound} controls></audio> */}
        <p>Type:{type}</p>
    </div>
  )
}

export default LetterCard