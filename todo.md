# List of Things to Do

The app is split into two so to speak. There is the main part which anyone can access and then the app itself (within the catalog folder) which is where the actual management of the shelter will happen.
This is why there is two template folders and there are two 'base.html' templates.

The base.html templates will be pulled through to the other templates.

## To do

### Backend

- Build testing
- Create Rest API
- Improve user registration so can determine who can create an account
- Possibly look at introducing a subdomain depending on shelter.
  - if doing this possibly tailor users to specific domains etc.

### Frontend

- Improve usability with Ajax
- Improve usability with JS

### Done

- Expand url routing
- Create views - Partly done
- Set up email
- Use environment variables for sensitive info
- Create Models
- Create animal
- Maintain animal (in part), see above about maintaining animal type, colour and species
- Delete animal
- List of all available animals
- Maintain animal type, colour and species = Should we split the Animal model so it only contains Species as char field. Breed is char field in its own model and
 colour remains in its own model but gets linked straight into AnimalInstance mode
- Complete design of base.html files needed (possibly use bootstrap or CSS grid)
- Allow import/export of data
- Creation of different pages