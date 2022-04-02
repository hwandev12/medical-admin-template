import PropTypes from 'prop-types';
import React from 'react';

const countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas"
  , "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "British Virgin Islands"
  , "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Chad", "Chile", "China", "Colombia", "Congo", "Cook Islands", "Costa Rica"
  , "Cote D Ivoire", "Croatia", "Cruise Ship", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "England", "Equatorial Guinea"
  , "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "French Polynesia", "French West Indies", "Gabon", "Gambia", "Georgia", "Germany", "Ghana"
  , "Gibraltar", "Greece", "Greenland", "Grenada", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India"
  , "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyz Republic", "Laos", "Latvia"
  , "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania"
  , "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia"
  , "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal"
  , "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "Saint Pierre and Miquelon", "Samoa", "San Marino", "Kingdom of Saudi Arabia", "Scotland", "Senegal", "Serbia", "Seychelles"
  , "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "South Africa", "South Korea", "Spain", "Sri Lanka", "St Kitts and Nevis", "St Lucia", "St Vincent", "St. Lucia", "Sudan"
  , "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor L'Este", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia"
  , "Turkey", "Turkmenistan", "Turks and Caicos", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay"
  , "Uzbekistan", "Venezuela", "Vietnam", "Virgin Islands (US)", "Wales", "Yemen", "Zambia", "Zimbabwe"];

export default class Control extends React.Component {
  static propTypes = {
    onChange: PropTypes.func.isRequired,
    forID: PropTypes.string,
    value: PropTypes.node,
    classNameWrapper: PropTypes.string.isRequired,
  }

  static defaultProps = {
    value: '',
  }

  getOptions() {
    const options = countries.map((i, index) =>
      (<option value={i.toLowerCase().replace(/ /g, '_')} key={index}>{i}</option>)
    );

    return options
  }

  render() {
    const {
      forID,
      value,
      onChange,
      classNameWrapper,
    } = this.props;

    console.log(this.props);

    return (
      <select
        id={forID}
        className={classNameWrapper}
        value={value || ''}
        onChange={e => onChange(e.target.value)}
      >
        {this.getOptions()}
      </select>
    );
  }
}
