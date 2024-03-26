import './minfotiles.css';

const Minfotile = (props) => {

    //Need to be exact name of passed dictionary
    const {DefaultGateway, LocalAddress, MACAddress, MachineName} = props.data;

    return(
    <div className="minfosec">
        <label className='mnlbl'>{MachineName}</label>
        <div className='minfo'>
        <label className='infolbl'>MAC Address: {MACAddress} </label>
        <label className='infolbl'>Default Gateway: {DefaultGateway} </label>
        <label className='infolbl'>Local Address: {LocalAddress} </label>
        </div>
    </div>
    )
}

export default Minfotile;
