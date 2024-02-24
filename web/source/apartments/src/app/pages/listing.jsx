import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-quartz.css";

import { useEffect, useState } from 'react';

import { AgGridReact } from 'ag-grid-react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

/*
Display apartment listing with all available entries form API
*/
function ApartmentsList() {

	const navigate = useNavigate();

	// Grid rows. empty till fetched from API
	const [rowData, setRowData] = useState([]);

	// Grid columns. with 'id' column hidden. only used when navigating to details
	const [colDefs, setColDefs] = useState([
		{ field: "number" },
		{ field: "floor" },
		{ field: "city" },
		{ field: "price" },
		{
			field: "id",
			hide: true,
			suppressToolPanel: true,
		},
	]);

	// get apartments from API, empty list if no entries in db
	useEffect(() => {
			axios.get('http://localhost:8000/app/apartments')
			.then(function (response) {
				setRowData(response.data);
				console.log(response);
			})
			.catch(function (error) {
				console.log(error);
			})
			.finally(function() {
				console.log('done');
			})
		},
		[]
	);

	// render apartments listig in ag-grid, if row clicked => navigate to details page of apartment
	return (
		<>
			<div className="ag-theme-quartz" style={{ height: 500 }}>
				<AgGridReact rowData={rowData} columnDefs={colDefs} onRowClicked={(e)=>navigate(`/${e.data.id}`)} />
			</div>
		</>
	);
}


export default ApartmentsList;