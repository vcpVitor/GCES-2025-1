import React from 'react';
import { render, screen } from '@testing-library/react';
import HomePage from '../pages/index';

describe('HomePage', () => {
  it('renders a heading', () => {
    render(<HomePage />);

    const heading = screen.getByRole('heading', {
      name: /welcome to the app/i,
    });

    expect(heading).toBeInTheDocument();
  });
});
