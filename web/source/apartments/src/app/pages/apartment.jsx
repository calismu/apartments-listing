import { useEffect, useState } from 'react';

import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';


// Component to render if /apartment/<id> had an invalid id (error message from API)
function ApartmentNotFound() {
	return (
		<CardContent>
			<Typography sx={{ mb: 0.5, fontSize: 20 }} variant="h5" component="div">
        Apartment Not Found
      </Typography>
      <Typography sx={{ mb: 0.5, fontSize: 10 }} color="text.secondary">
        The apartment you're looking for does not exist, please head back to listing page
      </Typography>
		</CardContent>
	);
}


// Displaying apartment details in a card (on success response from server), takes in apartment object as prop
function ApartmentCard({ apartment }) {
	return (
    <CardContent>
      <Typography sx={{ mb: 2, fontSize: 14 }} color="text.secondary" gutterBottom>
      	Apartment {apartment.id}
      </Typography>
      <Typography sx={{ mb: 0.5, fontSize: 20 }} variant="h5" component="div">
        Address
      </Typography>
      <Typography sx={{ mb: 0.5, fontSize: 10 }} color="text.secondary">
        {`apt. ${apartment.number}, floor ${apartment.floor}, building ${apartment.building}`}
      </Typography>
      <Typography sx={{ mb: 3, fontSize: 10}} color="text.secondary">
        {`${apartment.city}, Egypt`}
      </Typography>
      <Typography sx={{ mb: 0.5, fontSize: 20 }} variant="h5" component="div">
        Area
      </Typography>
      <Typography sx={{ mb: 3, fontSize: 10 }} color="text.secondary">
        {apartment.area_m2} m<sup>2</sup>
      </Typography>
      <Typography sx={{ mb: 0.5, fontSize: 20 }} variant="h5" component="div">
        Price
      </Typography>
      <Typography sx={{ mb: 3, fontSize: 10 }} color="text.secondary">
        ${Math.trunc(apartment.price)}
      </Typography>
      <Typography sx={{ fontSize: 10 }} style={{ maxWidth: '25rem' }} variant="body2">
        {apartment.description}
      </Typography>
    </CardContent>
	);
}


// Main component renders apartment card OR not found page, with 'back to listing' link
function Apartment() {

	const { id } = useParams(); // apartment id privided by apartments/id
	const navigate = useNavigate();

	const [apartment, setApartment] = useState({}); // apartment object from API

	// Call API to get apartment. set apartment object on success, or to null on error
	// apartment value, decides what to render in JSX
	useEffect(() => {
			axios.get(`http://localhost:8000/app/apartments/${id}`)
			.then(function (response) {
				setApartment(response.data);
				console.log(response);
			})
			.catch(function (error) {
				setApartment(null);
				console.log(error);
			})
			.finally(function() {
				console.log('done');
			})
		},
		[]
	);

	// render card or not found based on apartment value
	return (
		<div>
			<Box sx={{ minWidth: 275 }}>
				<Card variant="outlined">
					{ (apartment !== null) ? <ApartmentCard apartment={apartment}/> : <ApartmentNotFound /> }
					<CardActions>
			      <Button size="small" onClick={()=>navigate('/')}>Back to Listing</Button>
			    </CardActions>
				</Card>
			</Box>
		</div>
	);
}

export default Apartment;