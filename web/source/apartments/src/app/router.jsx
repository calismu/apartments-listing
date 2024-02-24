import { BrowserRouter, Routes, Route } from 'react-router-dom';

import ApartmentsList from './pages/listing';
import Apartment from './pages/apartment';


/*
Router for:
/apartments => to get all apartments in listing
/apartments/<apartment-id> => to get a single apartment
*/

export default function Router() {
	return (
		<BrowserRouter basename="/apartments">
			<Routes>
				<Route path="/" element={<ApartmentsList/>} />
				<Route path="/:id" element={<Apartment/>} />
			</Routes>
		</BrowserRouter>
	);
};