import React from 'react'
const ToggleSwitch = (props : any) => {
    const [isChecked, setIsChecked] = React.useState(props.isChecked);
    const handleToggle = () => {
        setIsChecked(!isChecked);
    }

    return (
    <div className="relative inline-block w-14 mr-2 align-middle select-none transition duration-200 ease-in">
        <label htmlFor="toggle" className="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer">
            <input type="checkbox" name="toggle" id="toggle" className="checked:bg-blue-500 bg-white toggle-checkbox absolute block w-6 h-6 rounded-full  border-4 appearance-none cursor-pointer" checked={isChecked} onChange={handleToggle}/>
        </label>
    </div>
    );
}
export default ToggleSwitch