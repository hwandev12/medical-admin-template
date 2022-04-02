import CountrySelectControl from './Control';
import CountrySelectPreview from './Preview';

if (typeof window !== 'undefined') {
  window.CountrySelectControl = CountrySelectControl;
  window.CountrySelectPreview = CountrySelectPreview;
}

const exportObject = {
  CountrySelectControl,
  CountrySelectPreview
};

export default exportObject;
